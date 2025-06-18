# blog/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.views import View 
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm 

from .forms import CustomUserCreationForm , BlogPostForm
from django.contrib.auth.mixins import LoginRequiredMixin,  UserPassesTestMixin
from django.views.generic import CreateView, UpdateView
from .models import BlogPost, Category 

from django.core.paginator import Paginator 
from django.db.models import Q 
from django.contrib import messages 
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseForbidden

from django.contrib.auth.decorators import login_required, user_passes_test


# Registration View handles the resgistration process of my new users
class RegisterView(View):
    template_name = 'registration/register.html'
    form_class = CustomUserCreationForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
       # checks if the form is valid if it is valid then save the user and login the user
       # if form is not valid then return the template wuth the form errors
        form = self.form_class(request.POST, request.FILES)
        print(form.is_valid(), form.errors)  
        if form.is_valid():
            user = form.save()
            login(request, user) 
            return redirect('home')
        return render(request, self.template_name, {'form': form})



class HomePageView(View):
    template_name = 'home.html'
    paginate_by = 5 # Number of posts per page

    def get(self, request, *args, **kwargs):
        posts = BlogPost.objects.filter(is_published=True).order_by('-published_date')

        # Category Filtering
        category_id = request.GET.get('category')
        if category_id:
            posts = posts.filter(categories__id=category_id)

        # Search Filtering (Title/Content)
        search_query = request.GET.get('q')
        if search_query:
            posts = posts.filter(
                Q(title__icontains=search_query) | Q(content__icontains=search_query)
            ).distinct() # .distinct() to avoid duplicate posts if they appear in multiple categories that match search

        # Pagination
        paginator = Paginator(posts, self.paginate_by)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'page_obj': page_obj,
            'categories': Category.objects.all().order_by('name'), # All categories for dropdown
            'selected_category': category_id, # To pre-select dropdown
            'search_query': search_query, # To pre-fill search box
        }
        return render(request, self.template_name, context)
    
class CreatePostView(LoginRequiredMixin, CreateView):
    model = BlogPost # Specifies the model this view creates
    form_class = BlogPostForm # Specifies the form to use
    template_name = 'posts/create_post.html' # Template to render
    success_url = reverse_lazy('home') # Where to redirect after successful post creation

    # This method is called when the form submitted via POST is valid
    def form_valid(self, form):
        
        form.instance.author = self.request.user
        # Make sure the user is authenticated before allowing to create a new post at the backend
        if not self.request.user or not self.request.user.is_authenticated:
                return HttpResponseForbidden("You must be logged in to create a post.")
        
        # Calling parent form valid method to save the form and to create post
        response = super().form_valid(form)

        messages.success(self.request, "Your blog post has been published!")

        # (redirect to success_url)
        return response

    # This method is called when the form submitted via POST is NOT valid
    def form_invalid(self, form):
        messages.error(self.request, "Please correct the errors below.")
        return super().form_invalid(form) # Render template with form errors

@login_required # User must be logged in

def update_blog_post(request, pk):
    # Get the post, or return 404.
    # The user_passes_test decorator already ensures it's the author's post.
    post = get_object_or_404(BlogPost, pk=pk) 
    if post.author != request.user:
         return HttpResponseForbidden("You are not allowed to edit this post.")
  
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()

            messages.success(request, "Your blog post has been updated!")
            return redirect('home')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        # For GET request to pre-populate the form with existing posts
        form = BlogPostForm(instance=post)
    
    context = {
        'form': form,
        'post': post,
        'all_categories': Category.objects.all().order_by('name'), # For rendering manual dropdown if needed
    }
    return render(request, 'posts/update_post.html', context)


#  Delete Post View
@login_required # User must be logged in
def delete_blog_post(request, pk):
    # Get the post. user_passes_test ensures it's the author's post.
    post = get_object_or_404(BlogPost, pk=pk)
    if post.author != request.user:
         return HttpResponseForbidden("You are not allowed to edit this post.")
    
    post.delete() # Delete the post from database
    messages.success(request, "Your blog post has been deleted!")
    return  redirect('home') 
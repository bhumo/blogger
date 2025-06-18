from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, BlogPost, Category, Comment

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

        fields = UserCreationForm.Meta.fields + ('email', 'avatar', 'bio',)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User

        fields = ('username', 'email', 'avatar', 'bio', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')


class BlogPostForm(forms.ModelForm):


    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'categories']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10}),
   
            'categories': forms.SelectMultiple(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
                'id': 'category-select' # Add an ID for JavaScript targeting
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['categories'].queryset = Category.objects.all().order_by('name')
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content'] # Only content will be entered by the user
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write your comment here...'}),
        }
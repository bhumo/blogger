from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, BlogPost, Category 

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        # Include your custom fields (email, avatar, bio)
        # UserCreationForm.Meta.fields already includes 'username' and 'password'
        fields = UserCreationForm.Meta.fields + ('email', 'avatar', 'bio',)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        # These fields are for admin or profile editing. Customize as needed.
        fields = ('username', 'email', 'avatar', 'bio', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')


class BlogPostForm(forms.ModelForm):


    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'categories']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10}),
            # CHANGE HERE: Use SelectMultiple for the categories dropdown
            'categories': forms.SelectMultiple(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
                'id': 'category-select' # Add an ID for JavaScript targeting
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['categories'].queryset = Category.objects.all().order_by('name')

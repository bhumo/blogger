# blog/urls.py

from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'), # Your home page with dynamic content
    path('register/', RegisterView.as_view(), name='register'), # Registration page
    path('post/new/', CreatePostView.as_view(), name='create_post'), #creating new post
    path('post/<int:pk>/edit/', update_blog_post, name='post_edit'),  # edit current user post
    path('post/<int:pk>/delete/', delete_blog_post, name='post_delete'), # delete current user post
]
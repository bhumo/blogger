# blog/urls.py

from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'), # Your home page with dynamic content
    path('register/', RegisterView.as_view(), name='register'), # Registration page
    path('post/new/', CreatePostView.as_view(), name='create_post'), #creating new post
]
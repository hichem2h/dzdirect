from django.urls import path
from .views import (index, post_details, post_details_upvote,
                    post_details_downvote, contact)

urlpatterns = [
    path('', index, name='home'),
    path('posts/<pk>', post_details, name='post_details'),
    path('posts/<pk>/upvote', post_details_upvote, name='post_details_upvote'),
    path('posts/<pk>/downvote', post_details_downvote, name='post_details_downvote'),
    path('contact', contact, name='contact'),
]

from django.urls import path
from .views import PostAPIViews, PostList
#PostDetailAPIView, PostUpdateAPIView, PostDeleteAPIView

urlpatterns = [
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostAPIViews.as_view()),
]
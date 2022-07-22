from django.urls import path

from .views import PostsAPIView, PostAPIView

urlpatterns = [

    path('post/', PostsAPIView.as_view()),
    path('post/<int:pk>/', PostAPIView.as_view())


]
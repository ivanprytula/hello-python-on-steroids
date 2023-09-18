from django.urls import path

from .views import PostDetailView

app_name = "posts"
urlpatterns = [
    path("posts/<int:pk>/", PostDetailView.as_view(), name="posts-detail"),
]

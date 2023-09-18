from django.urls import path

from apps.users.views import UserDetailView, UserRedirectView, UserUpdateView

app_name = "users"
urlpatterns = [
    path("~redirect/", UserRedirectView.as_view(), name="redirect"),
    path("~update/", UserUpdateView.as_view(), name="update"),
    path("<int:pk>/", UserDetailView.as_view(), name="detail"),
]

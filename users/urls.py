from django.urls import path
from rest_framework_simplejwt import views

from users import views as user_views

urlpatterns = [
    path("users/", user_views.UserView.as_view()),
    path("users/login/", views.TokenObtainPairView.as_view()),
    path("users/<int:user_id>/", user_views.UserDetailView.as_view()),
]

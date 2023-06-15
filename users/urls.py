from django.urls import path
from rest_framework_simplejwt import views

from .views import UserView

urlpatterns = [
    path("users/", UserView.as_view()),
    path("users/login/", views.TokenObtainPairView.as_view()),
]

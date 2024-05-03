from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView

urlpatterns = [
    path("signup/", views.SignUpAPIView.as_view(), name="signup"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("logout/", TokenBlacklistView.as_view(), name="token_blacklist"),
    path("<str:username>/", views.ProfileAPIView.as_view(), name="profile"),
    path("login/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
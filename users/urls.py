from django.urls import path
from . import views

urlpatterns = [
    path("<str:username>/", views.ProfileAPIView.as_view(), name="profile"),
]
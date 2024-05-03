from django.urls import path
from . import views

app_name = "articles"
urlpatterns = [
    path("", views.ArticleListAPIView.as_view(), name="article_list"),
    # path("<int:pk>/", views.article_detail, name="aricle_detail"),
]
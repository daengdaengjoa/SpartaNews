from django.urls import path
from . import views

app_name = "articles"
urlpatterns = [
    path("", views.ArticleListAPIView.as_view(), name="article_list"),
    path("<int:pk>/", views.ArticleDetailAPIView.as_view(), name="aricle_detail"),
    path("<int:pk>/like/", views.LikeAPIView.as_view(), name="like"),
    path('api/comments', views.create_comment, name='create_comment'),
    path('api/comments', views.list_comments, name='list_comments'),
    path('api/comments/<int:comment_id>', views.update_or_delete_comment, name='update_or_delete_comment'),
    path('api/comments/<int:comment_id>/like', views.like_comment, name='like_comment'),
]
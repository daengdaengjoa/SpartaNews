from django.urls import path
from . import views

app_name = "articles"
urlpatterns = [
    path("", views.ArticleListAPIView.as_view(), name="article_list"),
    path("create/", views.ArticleListAPIView.as_view(), name="article_create"),   
    path("<int:pk>/like/", views.LikeAPIView.as_view(), name="like"),
    path("<int:pk>/comments/", views.CommentAPIView.as_view(), name="comments"),
    path('<int:pk>/comments/<int:comment_id>/', views.CommentDetailAPIView.as_view(), name='comment_detail'),
    path('<int:pk>/comments/<int:comment_id>/like/', views.CommentLikeAPIView.as_view(), name='comment_like'),
]
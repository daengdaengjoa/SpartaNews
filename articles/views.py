from django.shortcuts import render, get_object_or_404
from django.core import serializers
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated #로그인 인증토큰
from .models import Article
from .serializer import ArticleSerializer



class ArticleListAPIView(APIView):
    def get_permissions(self):#로그인 인증토큰
        permissions = super().get_permissions()

        if self.request.method.lower() == 'post': #포스트할때만 로그인
            permissions.append(IsAuthenticated())

        return permissions
    
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class ArticleDetailAPIView(APIView):
    def get_permissions(self): #로그인 인증토큰
        permissions = super().get_permissions()

        if self.request.method.lower() == ('put' or 'delete'):
            permissions.append(IsAuthenticated())

        return permissions
    
    def get_object(self, pk):
        return get_object_or_404(Article, pk=pk)

    def get(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        data = {"pk": f"{pk} is deleted."}
        return Response(data, status=status.HTTP_200_OK)

def index(request):
    sort_by = request.GET.get("sort", None)

    if sort_by == "popular":
        articles = Article.objects.order_by("-view_count")
    # elif sort_by == "newest":
    #     items = Item.objects.order_by("-created_at")
    # elif sort_by == "liked":
    #     items = Item.objects.annotate(like_count=Count("liked_by")).order_by(
    #         "-like_count"
    #     )
    else:
        articles = Article.objects.order_by("-created_at")

    return render(request, "newsplace/index.html", {"articles": articles})

from django.shortcuts import render, get_object_or_404
from django.core import serializers
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated  # 로그인 인증토큰
from .models import Article
from .serializer import ArticleSerializer
from django.db.models import Count
from django.core.paginator import Paginator


class ArticleListAPIView(APIView):
    def get_permissions(self):  # 로그인 인증토큰
        permissions = super().get_permissions()

        if self.request.method.lower() == 'post':  # 포스트할때만 로그인
            permissions.append(IsAuthenticated())

        return permissions

    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        request.data["username"] = request.user.username
        serializer = ArticleSerializer(data=request.data)
        # serializer.data["username"] = request.user.username #작성시 username 불러오기
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class ArticleDetailAPIView(APIView):
    def get_permissions(self):  # 로그인 인증토큰
        permissions = super().get_permissions()

        if self.request.method.lower() == ('put' or 'delete'):
            permissions.append(IsAuthenticated())

        return permissions

    def get_object(self, pk):
        return get_object_or_404(Article, pk=pk)
    

    def get(self, request, pk):
        article = self.get_object(pk)
        article.view_count += 1 #아티클 뷰수 조회
        article.save() #아티클 뷰수 조회
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, pk):
        article = self.get_object(pk)
        if request.user.username == article.username:#게시글 작성자 동일시 작성가능
            serializer = ArticleSerializer(
                article, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST) #게시글 작성자 동일시 작성가능

    def delete(self, request, pk):
        article = self.get_object(pk)
        if request.user.username == article.username:#게시글 작성자 동일시 작성가능
            article.delete()
            data = {"pk": f"{pk} is deleted."}
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST) #게시글 작성자 동일시 작성가능


class LikeAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        if article.like_users.filter(pk=request.user.pk).exists():
            article.like_users.remove(request.user)
            return Response("안좋아요", status=status.HTTP_200_OK)
        else:
            article.like_users.add(request.user)
            return Response("좋아요", status=status.HTTP_200_OK)
        # return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))



def index(request):
    sort_by = request.GET.get("sort", None)

    if sort_by == "popular":
        articles = Article.objects.order_by("-view_count")
    elif sort_by == "newest":
        articles = Article.objects.order_by("-created_at")
    elif sort_by == "liked":
        articles = Article.objects.annotate(like_count=Count("like_users")).order_by(
            "-like_count"
        )
    else:
        articles = Article.objects.order_by("-created_at")
    
    per_page = 3

    # Paginator 객체 생성
    paginator = Paginator(articles, per_page)

    # 요청된 페이지 번호 가져오기. 기본값은 1
    page_number = request.GET.get('page', 1)

    # 해당 페이지의 기사 목록 가져오기
    page_articles = paginator.get_page(page_number)

    return render(request, "newsplace/index.html", {"page_articles": page_articles})

from django.shortcuts import redirect, render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated  # 로그인 인증토큰
from .models import Article, Comment
from .serializer import ArticleSerializer, CommentSerializer
from django.db.models import Count, F, ExpressionWrapper, FloatField
from django.core.paginator import Paginator
from django.http import QueryDict
from django.db.models import Q


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
        article.view_count += 1  # 아티클 뷰수 조회
        article.save()  # 아티클 뷰수 조회
        serializer = ArticleSerializer(article)
        comments = Comment.objects.filter(article=article)
        return render(request, 'newsplace/detail.html', {'article': article, 'comments': comments})


    def put(self, request, pk):
        article = self.get_object(pk)
        if request.user.username == article.username:  # 게시글 작성자 동일시 작성가능
            serializer = ArticleSerializer(
                article, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        else:
            # 게시글 작성자 동일시 작성가능
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article = self.get_object(pk)
        if request.user.username == article.username:  # 게시글 작성자 동일시 작성가능
            article.delete()
            data = {"pk": f"{pk} is deleted."}
            return Response(data, status=status.HTTP_200_OK)
        else:
            # 게시글 작성자 동일시 작성가능
            return Response(status=status.HTTP_400_BAD_REQUEST)


class LikeAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        if article.like_users.filter(pk=request.user.pk).exists():
            # if request.user in article.like_users.all():
            article.like_users.remove(request.user)
            return Response("안좋아요", status=status.HTTP_200_OK)
        else:
            article.like_users.add(request.user)
            return Response("좋아요", status=status.HTTP_200_OK)


class CommentAPIView(APIView):
    def get_permissions(self):  # 로그인 인증토큰
        permissions = super().get_permissions()

        if self.request.method.lower() == 'post':  # 포스트할때만 로그인
            permissions.append(IsAuthenticated())

        return permissions

    def get(self, request, pk):
        comments = Comment.objects.all().filter(article=pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        request.data["user"] = request.user.pk
        request.data["article"] = article.id
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class CommentDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def put(self, request, pk, comment_id):
        comment = get_object_or_404(Comment, pk=comment_id)
        if request.user == comment.user:
            serializer = CommentSerializer(comment, data=request.data, partial=True)
            print(serializer)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, comment_id):
        comment = get_object_or_404(Comment, pk=comment_id)
        if request.user == comment.user:
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class CommentLikeAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk, comment_id):
        comment = get_object_or_404(Comment, pk=comment_id)
        if comment.like_users.filter(pk=request.user.pk).exists():
            # if request.user in comment.like_users.all():
            comment.like_users.remove(request.user)
            return Response("안좋아요", status=status.HTTP_200_OK)
        else:
            comment.like_users.add(request.user)
            return Response("좋아요", status=status.HTTP_200_OK)


def index(request):
    sort_by = request.GET.get("sort", None)
    query = request.GET.get("query", None)

    articles = Article.objects.all()

    if query:
        articles = articles.filter(
            Q(title__icontains=query) |  # 제목 검색
            Q(content__icontains=query) |  # 내용 검색
            Q(username__icontains=query)  # 작성자 이름 검색
        )

    if not query: 
        if sort_by == "popular":
            articles = articles.order_by("-view_count")
        elif sort_by == "newest":
            articles = articles.order_by("-created_at")
        elif sort_by == "liked":
            articles = articles.annotate(like_count=Count("like_users")).order_by("-like_count")
        elif sort_by == "rank":
            articles = articles.annotate(rank=ExpressionWrapper(Count('like_users') * 5 + F('view_count'), output_field=FloatField())).order_by('-rank', '-created_at')
        else:
            articles = articles.order_by("-created_at")
    else: 
        pass

    per_page = 3
    paginator = Paginator(articles, per_page)
    page_number = request.GET.get('page', 1)

    next_page_query = QueryDict(mutable=True)
    next_page_query['sort'] = sort_by if sort_by else None
    next_page_query['query'] = query if query else None

    page_articles = paginator.get_page(page_number)
    page_articles.next_page_query = next_page_query.urlencode()

    return render(request, "newsplace/index.html", {
        "page_articles": page_articles,
        "query": query,
    })
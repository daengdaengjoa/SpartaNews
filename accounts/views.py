from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password
from .serializers import UserSerializer
from .models import User


class SignUpAPIView(APIView):
    def post(self, request):
        request.data['password'] = make_password(request.data['password'])
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response("회원가입 완료!", status=status.HTTP_201_CREATED)


class ProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, username):
        profile = get_object_or_404(User, username=username)
        serializer = UserSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)

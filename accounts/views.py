from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404

from .models import User
from .serializers import UserSerializer


class SignUpAPIView(APIView):
    def post(self, request):
        request.data['password'] = make_password(request.data['password'])
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProfileAPIView(APIView):
    pass

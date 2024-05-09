from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from accounts.serializers import UserSerializer


class ProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, username):
        if request.user.username == username:
            profile = get_object_or_404(get_user_model(), username=username)
            serializer = UserSerializer(profile)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        extra_kwargs = {
            'like_users': {'required': False}, #제외시켜주는함수
        }

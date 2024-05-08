from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    
    CATEGORY_CHOICES = [
        
        ("technology", "Technology"),
        ("AI", "AI"),
        ("Life", "Life"),
        ("hobby", "Hobby"),
        
    ]
    
    class Meta:
        model = Article
        fields = "__all__"
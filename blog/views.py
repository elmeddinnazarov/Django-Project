from django.shortcuts import render
from .models import Article
# Create your views here.


def blog_list(request):
    articles = Article.objects.all()
    return render(request, 'blog.html', context={'articles': articles})

def blog_detail(request, id):
    article = Article.objects.get(id=id)
    return render(request, 'article.html', context={'article': article})
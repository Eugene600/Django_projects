from django.shortcuts import render
from .models import Article
from django.http import HttpResponse

# Create your views here.
def articles(request):
    article = Article.objects.all().order_by('date_published')
    return render(request, 'articles/articles.html', {'article': article})

def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request,'articles/article_detail.html',{'art':article})
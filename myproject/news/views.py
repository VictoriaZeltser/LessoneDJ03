from django.shortcuts import render
from .models import News_post

def home(request):
    news = News_post.objects.all()  # Получаем все новости
    return render(request, 'news/news.html', {'news': news})  # Передаем новости в шаблон

from django.shortcuts import render
from .models import mainNews, cardNews

# Create your views here.
def index(request):
    news = mainNews.objects.all()
    cards = cardNews.objects.all()
    context = {
        'news': news,
        'cards': cards,
    }
    return render(request, 'block/index.html', context)
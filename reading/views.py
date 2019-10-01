from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index_of_reading.html')

def article(request):
    return render(request, 'article.html')

def detail(request, slug):
    return render(request, 'detail_of_article.html')
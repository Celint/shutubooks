from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index_of_reading.html')
    
def detail(request):
    return render(request, 'detail_of_article.html')

def mine(request):
    return render(request, 'myarticles.html')
    
def books(request):
    return render(request, 'mybooks.html')

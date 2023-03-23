from django.shortcuts import render


# Create your views here.
def berners_lee(request):
    return render(request, 'articles/berners_lee.html')
def index(request):
    return render(request, 'index.html')
from django.shortcuts import render

# Create your views here.
app_name = ''
def index(request):
    return render(request, 'index.html')
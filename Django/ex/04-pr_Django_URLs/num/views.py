from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'num/index.html')
def number_print(request, number):
    context = {
        'number': number,
    }
    return render(request, 'num/number_print.html', context)
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'calcul/index.html')


def calculate(request, num1, num2):
    context = {
        'num1': num1,
        'num2': num2,
        'plus': num1 + num2,
        'minus': num1 - num2,
        'multiply': num1 * num2,
        'divide': num1 // num2,
    }
    return render(request, 'calcul/calculate.html', context)
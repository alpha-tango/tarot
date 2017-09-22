from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'learn/index.html')

def symbolism(request):
    return render(request, 'learn/symbolism.html')

def tips(request):
    return render(request, 'learn/tips.html')

def layouts(request):
    return render(request, 'learn/layouts.html')

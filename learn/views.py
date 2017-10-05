from django.shortcuts import render
from django.views.generic.list import ListView
from learn.models import Suit

# Create your views here.

def index(request):
    return render(request, 'learn/index.html')

class SuitList(ListView):
    model = Suit

def symbolism(request):
    return render(request, 'learn/symbolism.html')

def tips(request):
    return render(request, 'learn/tips.html')

def layouts(request):
    return render(request, 'learn/layouts.html')

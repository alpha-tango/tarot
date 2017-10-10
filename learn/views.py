from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from learn.models import Suit, MinorArcana, Rank

# Create your views here.

def index(request):
    return render(request, 'learn/index.html')

class SuitList(ListView):
    model = Suit

class SuitDetail(DetailView):
    model = Suit

class RankList(ListView):
    model = Rank

class RankDetail(DetailView):
    model = Rank

class MinorArcanaDetail(DetailView):
    model = MinorArcana

def symbolism(request):
    return render(request, 'learn/symbolism.html')

def tips(request):
    return render(request, 'learn/tips.html')

def layouts(request):
    return render(request, 'learn/layouts.html')

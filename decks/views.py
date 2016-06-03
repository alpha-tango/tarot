from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Deck, Card

class IndexView(generic.ListView):
    template_name = 'decks/index.html'
    context_object_name = 'latest_deck_list'

    def get_queryset(self):
        return Deck.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Deck
    template_name = 'decks/detail.html'

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Deck, Card
from .forms import NewDeck, NewCard

class IndexView(generic.ListView):
    template_name = 'decks/index.html'
    context_object_name = 'latest_deck_list'

    def get_queryset(self):
        return Deck.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Deck
    template_name = 'decks/detail.html'

def new_deck(request):
    if request.method == 'POST':
        form = NewDeck(request.POST)
        if form.is_valid():
            deck = Deck(**form.cleaned_data)
            deck.save()
            return HttpResponseRedirect('/decks/')
    else:
        form = NewDeck()
    return render(request, 'decks/create_deck.html', {'form': form})

def new_card(request, pk):
    deck = Deck.objects.filter(pk=pk).first()
    if request.method == 'POST':
        form = NewCard(request.POST)
        if form.is_valid():
            card = Card(deck=deck, **form.cleaned_data)
            card.save()
            return HttpResponseRedirect(reverse('decks:detail', args=(deck.id,)))
    else:
        form = NewCard()
    return render(request, 'decks/create_card.html', {'form': form})

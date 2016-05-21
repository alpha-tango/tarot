from django.shortcuts import get_object_or_404, render
from .models import Deck

def index(request):
	latest_deck_list = Deck.objects.order_by('-pub_date')[:10]
	context = {
		'latest_deck_list': latest_deck_list,
	}
	return render(request, 'tarot_app/index.html', context)

def detail(request, deck_id):
	deck = get_object_or_404(Deck, pk=deck_id)
	return render(request, 'tarot_app/detail.html', {'deck': deck})

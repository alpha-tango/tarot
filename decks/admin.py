from django.contrib import admin

from .models import Deck
from .models import Card

admin.site.register(Deck)
admin.site.register(Card)

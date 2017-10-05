from django.contrib import admin

from learn.models import (
    Suit,
    Rank,
    MinorArcana,
    MajorArcana
)

admin.site.register(Suit)
admin.site.register(Rank)
admin.site.register(MinorArcana)
admin.site.register(MajorArcana)

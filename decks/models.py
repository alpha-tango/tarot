from __future__ import unicode_literals

from django.db import models

class Deck(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    def __str__(self):
        return self.name

class Card(models.Model):
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    image_url = models.CharField(max_length=200)

    def __str__(self):
        return self.name

from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Suit(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return '%s' % (self.name)

class Rank(models.Model):
    number = models.PositiveIntegerField()
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return '%s' % (self.name)

class MinorArcana(models.Model):
    rank = models.ForeignKey(Rank)
    suit = models.ForeignKey(Suit)
    description = models.TextField()

    def __str__(self):
        return '%s of %s' % (self.rank, self.suit)

MAJOR_RANK_CHOICES = [
(0, 'The Fool'),
(1, 'The Magician'),
(2, 'The High Priestess'),
(3, 'The Empress'),
(4, 'The Emperor'),
(5, 'The Hierophant'),
(6, 'The Lovers'),
(7, 'The Chariot'),
(8, 'Strength'),
(9, 'The Hermit'),
(10, 'Wheel of Fortune'),
(11, 'Justice'),
(12, 'The Hanged Man'),
(13, 'Death'),
(14, 'Temperance'),
(15, 'The Devil'),
(16, 'The Tower'),
(17, 'The Star'),
(18, 'The Moon'),
(19, 'The Sun'),
(20, 'Judgement'),
(21, 'The World')
]

class MajorArcana(models.Model):
    number = models.IntegerField(choices=MAJOR_RANK_CHOICES)
    description = models.TextField()

    def __str__(self):
        return '%s' % (number)

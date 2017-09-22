from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

################################################################################
# Users
################################################################################

COPYRIGHT_CHOICES = []

class Profile(models.Model):
    user = models.OneToOneField(User)
    credit_line = models.TextField()
    copyright_owner = models.TextField()
    copyright_status = models.IntegerField(choices=COPYRIGHT_CHOICES)
    hide_from_searches = models.BooleanField()
    allow_pinning = models.BooleanField()

    # copyright status
    # hide stuff from searches

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

################################################################################
# Decks
################################################################################

class Deck(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    curator = models.ForeignKey(Profile)
    is_published = models.BooleanField(blank=True)
    published_at = models.DateTimeField(auto_now_add=True, blank=True)

################################################################################
# Cards
################################################################################

MINOR_CHOICES = [
(1, 'Ace'),
(2, 'Two'),
(3, 'Three'),
(4, 'Four'),
(5, 'Five'),
(6, 'Six'),
(7, 'Seven'),
(8, 'Eight'),
(9, 'Nine'),
(10, 'Ten'),
(11, 'Page'),
(12, 'Knight'),
(13, 'Queen'),
(14, 'King'),
]

MAJOR_CHOICES = [
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

SUIT_CHOICES = [
(1, 'Swords'),
(2, 'Cups'),
(3, 'Wands'),
(4, 'Pentacles')
]

class Card(models.Model):
    creator = models.ForeignKey(Profile)
    description = models.TextField(null=True, blank=True)
    image_link = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    decks = models.ManyToManyField(Deck)
    creator_only = models.BooleanField()

    class Meta:
        abstract = True

class GenericCard(Card):
    name = models.CharField(max_length=100)
    number = models.PositiveIntegerField(null=True, blank=True)
    custom_designation = models.CharField(max_length=50, null=True, blank=True)
    # unique on name, number, custom_designation, deck

class MinorArcana(Card):
    suit = models.IntegerField(choices=SUIT_CHOICES)
    rank = models.IntegerField(choices=MINOR_CHOICES)
    # unique on suit, rank, deck

class MajorArcana(Card):
    number = models.IntegerField(choices=MAJOR_CHOICES)
    # unique on number, deck

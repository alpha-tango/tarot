from django import forms

class NewDeck(forms.Form):
    name = forms.CharField(label='Deck name', max_length=200)
    description = forms.CharField(label='Enter a brief description of your deck (500 character max)', max_length=500)

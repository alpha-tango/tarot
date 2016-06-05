from django.conf.urls import url

from . import views

app_name = 'decks'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^new_deck', views.new_deck, name='new_deck'),
    url(r'^(?P<pk>[0-9]+)/new_card', views.new_card, name='new_card')
]

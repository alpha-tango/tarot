from django.conf.urls import url

from . import views

app_name='tarot_app'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<deck_id>[0-9]+)/$', views.detail, name='detail')
]

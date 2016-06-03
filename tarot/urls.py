from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^decks/', include('decks.urls')),
    url(r'^admin/', admin.site.urls),
]

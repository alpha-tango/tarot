from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url('^tarot/', include('tarot.urls', namespace="tarot")),
    url('^learn/', include('learn.urls', namespace="learn")),
    url(r'^admin/', admin.site.urls),
]

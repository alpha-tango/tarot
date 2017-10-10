from django.conf.urls import include, url
from django.contrib import admin
from website import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('^tarot/', include('tarot.urls', namespace="tarot")),
    url('^learn/', include('learn.urls', namespace="learn")),
    url(r'^admin/', admin.site.urls),
]

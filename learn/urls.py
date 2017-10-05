from django.conf.urls import url
from django.contrib import admin
from learn import views

urlpatterns = [
    url(r'^suits$', views.SuitList.as_view(), name='suit-list'),
    url(r'^symbolism$', views.symbolism, name='symbolism'),
    url(r'^tips$', views.tips, name='tips'),
    url(r'^layouts$', views.layouts, name='layouts'),
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
]

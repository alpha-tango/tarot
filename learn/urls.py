from django.conf.urls import url
from django.contrib import admin
from learn import views

urlpatterns = [
    url(r'^suits$', views.SuitList.as_view(), name='suit-list'),
    url(r'^suits/(?P<pk>[\d]+)/?$', views.SuitDetail.as_view(), name='suit-detail'),
    url(r'^ranks$', views.RankList.as_view(), name='rank-list'),
    url(r'^ranks/(?P<pk>[\d]+)/?$', views.RankDetail.as_view(), name='rank-detail'),
    url(r'^minor-arcana$', views.MinorArcanaList.as_view(),
    name='minorarcana-list'),
    url(r'^minor-arcana/(?P<pk>[\d]+)/?$', views.MinorArcanaDetail.as_view(),
    name='minorarcana-detail'),
    url(r'^symbolism$', views.symbolism, name='symbolism'),
    url(r'^tips$', views.tips, name='tips'),
    url(r'^layouts$', views.layouts, name='layouts'),
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
]

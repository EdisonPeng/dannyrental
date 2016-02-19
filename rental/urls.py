from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^rooms/$', views.rooms, name='rooms'),
    url(r'^reservation/$', views.reservation, name='reservation'),
]

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.aboutus, name='about'),
    url(r'^tellus/$', views.tellus, name='tellus'),
    url(r'^joinus/$', views.joinus, name='joinus'),
    url(r'^harassment/$', views.harassment, name='harassment'),
]

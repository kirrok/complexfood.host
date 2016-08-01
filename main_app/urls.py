from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^base$', views.base, name='base'),
    url(r'^menu$', views.menu, name='menu'),
    url(r'^set_info(\d{1})/$', views.set_info, name='set_info'),
    url(r'^learn_more$', views.learn_more, name='learn_more'),
    url(r'^questions$', views.questions, name='questions'),
    url(r'^feedback$', views.feedback, name='feedback'),
    url(r'^contacts$', views.contacts, name='contacts'),
]

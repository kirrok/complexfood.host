from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^base$', views.base, name='base'),
    url(r'^menu$', views.menu, name='menu'),
    url(r'^set_info(\d{1})/$', views.set_info, name='set_info'),
    url(r'^learn_more$', views.learn_more, name='learn_more'),
    url(r'^faq$', views.faq, name='faq'),
    url(r'^feedback$', views.feedback, name='feedback'),
    url(r'^contacts$', views.contacts, name='contacts'),
    url(r'^checkout(\d{1})(\d{1})$', views.checkout, name='checkout'),
    url(r'^checkout$', views.checkout, name='checkout'),
    url(r'^thanks(\d{1})(\d{1})$', views.thanks, name='thanks'),
    url(r'^thanks_feedback$', views.thanks, name='thanks_feedback'),
    url(r'^backend_orders$', views.backend_orders, name='backend_orders'),
    url(r'^pfc$', views.pfc, name='pfc'),
]

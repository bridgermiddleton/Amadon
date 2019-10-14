from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^checkout/(?P<id>\d+)$', views.checkout),
    url(r'checkoutdata', views.checkoutdata),
    url(r'reset$', views.reset)
]
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.root),
    url(r'^jobnum-search/$', views.jobnum_search, name='jobnum_search'),
    url(r'^jobdetails/$', views.jobdetails, name='jobdetails'),
]
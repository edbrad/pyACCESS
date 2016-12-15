from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^jobnum-search/$', views.joblist, name='jobnum_search'),
    url(r'^job-details/([\w\-]+)$', views.jobdetails, name='job_details'),
]
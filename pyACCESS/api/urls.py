from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.root),
    url(r'^jobnum-search/$', views.jobnum_search, name='jobnum_search'),
    url(r'^jobdetails/$', views.jobdetails, name='jobdetails'),
    url(r'^companies/$', views.companies, name='companies'),
    url(r'^jobs-company/$', views.jobs_company, name='jobs_company'),
    url(r'^stats/$', views.stats, name='stats')
]
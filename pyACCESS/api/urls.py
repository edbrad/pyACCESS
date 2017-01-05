from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.root),
    url(r'^jobnum-search/([\w\-]+)$', views.joblist, name='jobnum_search'),
]
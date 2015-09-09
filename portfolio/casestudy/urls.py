from django.conf.urls import url

from . import views
## r = treat the following as a regular expression
## ^ = start of the string
## $ = end of the string
urlpatterns = [
   url(r'^$', views.IndexView.as_view(), name = 'index'),
   url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name = "detail"),
]

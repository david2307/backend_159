from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^persons/$', views.PersonList().as_view()),
    url(r'^registergcm/(?P<pk>[0-9]+)/$', views.RegisterGcm.as_view()),
    url(r'^login/$', views.Login.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
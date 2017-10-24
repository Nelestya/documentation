from django.conf.urls import url, include
from .views import *


app_name = 'documentation'
urlpatterns = [
    url(r'^$', HomeDoc.as_view(), name='home'),
    url(r'^(?P<category>[a-z]+)$', CategoryPage.as_view(), name='category'),
    url(r'^(?P<category>[a-z]+)/(?P<documentation>\d+)/$', DocumentationPage.as_view(), name='documentation'),

]

from django.conf.urls import url, include

from home.views import *

app_name = 'home'
urlpatterns = [
    # prototype
    # url(r'^$', views.index, name='index'),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^sorting/$', SortingPageView.as_view(), name='sorting'),
    url(r'^search/$', SearchPageView.as_view(), name='search'),
]

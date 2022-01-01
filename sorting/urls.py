from django.conf.urls import url, include

from sorting.views import *

app_name = 'sorting'
urlpatterns = [
    # prototype
    # url(r'^$', views.index, name='index'),
    url(r'^$', SortingPageView.as_view(), name='main'),
]

from django.conf.urls import url
from .views import search, TVShowPage, Save_like

app_name = 'LikeSeries'
urlpatterns = [
    # ex: /LikeSeries/
    url(r'^$', search, name = 'index'),
    url(r'^TVShow_page/(?P<tv_id>\d+)/$', TVShowPage, name='TVShow_page'),
    url(r'^TVShow_page/$', Save_like, name ='TVShowPage')
]

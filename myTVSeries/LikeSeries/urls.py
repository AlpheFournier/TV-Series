from django.conf.urls import url
from .views import search, TVShow_pageView, Save_like

app_name = 'LikeSeries'
urlpatterns = [
    # ex: /LikeSeries/
    url(r'^$', search, name = 'index'),
    url(r'^TVShow_page/$', TVShow_pageView, name='TVShow_page'),
    url(r'^TVShow_page/$', Save_like, name ='TVShowPage')
]

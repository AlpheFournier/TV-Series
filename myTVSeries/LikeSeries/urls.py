from django.conf.urls import url
from . import views

app_name = 'LikeSeries'
urlpatterns = [
    # ex: /LikeSeries/
    url(r'^$', views.search, name = 'index'),
    url(r'^TVShow_page/$', views.TVShow_pageView, name='TVShow_page'),
    url(r'^TVShow_page/$', views.Save_like, name ='TVShowPage')
]

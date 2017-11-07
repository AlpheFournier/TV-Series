from django.conf.urls import url
from . import views

app_name = 'LikeSeries'
urlpatterns = [
    # ex: /LikeSeries/
    url(r'^$', views.IndexView, name='index'),
    url(r'^TVShow_page/$', views.TVShow_pageView, name="TVShow_page"),
    url(r'^results/$', views.ResultsView, name="results"),
    url(r'^search/$', views.search, name="search")
]

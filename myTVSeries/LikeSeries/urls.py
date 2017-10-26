from django.conf.urls import url
from . import views

app_name = 'LikeSeries'
urlpatterns = [
    # ex: /LikeSeries/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /LikeSeries/5/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /LikeSeries/5/results/
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^add_TVShow_form/$', views.add_TVShow_form, name="add_TVShow_form"),
    # ex: /LikeSeries/5/like/
    url(r'^(?P<question_id>[0-9]+)/like/$', views.like, name='like'),
]

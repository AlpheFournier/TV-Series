from django.conf.urls import url
from . import views

app_name = 'LikeSeries'
urlpatterns = [
    # ex: /LikeSeries/
    url(r'^$', views.IndexView, name='index'),
    url(r'^add_TVShow_form/$', views.add_TVShow_form, name="add_TVShow_form"),
]

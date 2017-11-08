# coding=utf-8

from django import forms
from .models import TVShow


#création du formulaire:

class TVShowForm(forms.ModelForm):
    class Meta:
        """ Assigning the order of the fields"""
        model = TVShow
        fields = ['tv_id', 'name', 'language', 'overview', 'vote_avg', 'director', 'genre']

class SearchForm(forms.ModelForm):
    pass


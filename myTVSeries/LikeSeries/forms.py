# coding=utf-8

from django import forms
from .models import TVShow


#création du formulaire:

class TVShowForm(forms.ModelForm):
    class Meta:
        """ Assigning the order of the fields"""
        model = TVShow
        fields = ["title", "director", "genre", "language","mark"]

class SearchForm(forms.ModelForm):
    pass
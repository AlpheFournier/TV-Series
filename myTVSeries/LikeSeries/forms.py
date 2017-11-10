# coding=utf-8

from django import forms
from .models import TVShow, Like


#création du formulaire:

class TVShowForm(forms.ModelForm):
    class Meta:
        """ Assigning the order of the fields"""
        model = TVShow
        fields = ['tv_id', 'title', 'language', 'overview', 'vote_avg', 'director', 'gender', 'actors']

class SearchForm(forms.ModelForm):
    pass

class LikeForm(forms.ModelForm):
    class Meta:
        model = Like
        fields = ['like_counter']

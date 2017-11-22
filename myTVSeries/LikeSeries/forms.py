# coding=utf-8

from django import forms
from .models import TVShow, UserLikes

#création du formulaire:

class TVShowForm(forms.ModelForm):
    class Meta:
        """ Assigning the order of the fields"""
        model = TVShow
        fields = ["title"]

class LikeForm(forms.ModelForm):
    class Meta:
        model = UserLikes
        fields = ["tv_id_liked",]

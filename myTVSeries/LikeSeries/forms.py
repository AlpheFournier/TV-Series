# coding=utf-8

from django import forms
from .models import TVShow, User_Likes

#création du formulaire:

class TVShowForm(forms.ModelForm):
    class Meta:
        """ Assigning the order of the fields"""
        model = TVShow
        fields = ["title"]

class LikeForm(forms.ModelForm):
    class Meta:
        model = User_Likes
        fields = ["like_action",]

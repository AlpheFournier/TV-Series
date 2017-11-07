# coding=utf-8

from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from .models import TVShow
from .forms import TVShowForm, SearchForm
from django.template import loader
import json
from django.contrib.auth import *

def home(request):
    return HttpResponse("Bienvenue sur MyTVSeries. Likes les séries que tu aimes!")

def IndexView(request):
    template = loader.get_template('LikeSeries/index.html')
    return HttpResponse(template.render(request=request))

def ResultsView(request):
    template = loader.get_template('LikeSeries/results.html')
    return HttpResponse(template.render(request=request))

def TVShow_pageView(request):
    template = loader.get_template('LikeSeries/TVShow_page.html')
    return HttpResponse(template.render(request=request))


#Fonction qui permet de liker une série et de rajouter une série à sa liste de séries likées:
def add_TVShow_form(request):
    series_liked=[]
    # si j'ai cliqué sur le bouton je le rajoute à la liste de séries likées
    if request.POST ():
        form = TVShowForm(request.POST)
        if form.is_valid():
            # On vérifie que la série existe déjà dans la base de données
            check_db = TVShow.objects.filter(title=request.POST['title'])
            if len(check_db) > 0:
                return render(request, 'LikeSeries/TVShow_page.html',
                              {'TVShow_title': request.POST['title']})
            else:
                # Save form and redirect to the success page
                form.save()
                return render_to_response('add_success.html',
                                          {'TVShow_title': request.POST['title']})
    else:
        form = TVShowForm()
    return render(request, 'LikeSeries/TVShow_page.html',
                  {'form': form})

# Pour chercher dans la base de données avec le titre de la série, le genre, le réalisateur, les notes etc...
def search(request):
    if request.GET:
        TVShow_listing = []
        search_string = ""
        if request.GET['title']:
            for TVShow_object in TVShow.objects.filter(title__contains=request.GET['title']):
                TVShow_dict = {'TVShow_object': TVShow_object}
                TVShow_listing.append(TVShow_dict)
            search_string = request.GET['title']
        if request.GET['genre']:
            for TVShow_object in TVShow.objects.filter(genre__contains=request.GET['genre']):
                TVShow_dict = {'TVShow_object': TVShow_object}
                TVShow_listing.append(TVShow_dict)
            search_string = " ".join((search_string, request.GET['genre']))
        if request.GET['director']:
            for TVShow_object in TVShow.objects.filter(director__contains=request.GET['director']):
                TVShow_dict = {'TVShow_object': TVShow_object}
                TVShow_listing.append(TVShow_dict)
            search_string = " ".join((search_string, request.GET['director']))
        if request.GET['language']:
            for TVShow_object in TVShow.objects.filter(language__contains=request.GET['language']):
                TVShow_dict = {'TVShow_object': TVShow_object}
                TVShow_listing.append(TVShow_dict)
            search_string = " ".join((search_string, request.GET['language']))
        if request.GET['mark']:
            for TVShow_object in TVShow.objects.filter(mark__contains=request.GET['mark']):
                TVShow_dict = {'TVShow_object': TVShow_object}
                TVShow_listing.append(TVShow_dict)
            search_string = " ".join((search_string, request.GET['mark']))
        if len(TVShow_listing) > 0:
            return render_to_response('LikeSeries/results.html', {'search_string': search_string,
                                                       'TVShow_listing': TVShow_listing})
    form = TVShowForm()
    return render(request,'LikeSeries/index.html', {'form': form})
'''
def search_serie(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            template = loader.get_template('LikeSeries/results.html')

            serie_id = api_call.Api_call.get_tv_id(request.POST['search'])
            response = []
            for i in range(0, len(serie_id)):
                response.append(api_call.Api_call.get_serie())
            context = {'response':response}
            return HttpResponse(template.render(request=request, context=context))
        else:
            raise EnvironmentError
    else:
        form = SearchForm()

    return render(request, 'LikeSeries/index.html', {'form':form})
'''

# coding=utf-8

from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from .models import TVShow
from .forms import TVShowForm, LikeForm
from django.template import loader
import json
from django.contrib.auth import *
import sys
sys.path.append("..")

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

"""
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
                  {'form': form})"""

# Pour chercher dans la base de données avec le titre de la série, le genre, le réalisateur, les notes etc...

def search(request):
    if request.method == 'POST':
        form = TVShowForm(request.POST)
        if form.is_valid():
            from myTVSeries import api_call
            api = api_call.Api_call()
            template = loader.get_template('LikeSeries/results.html')
            serie_id = api.get_tv_id(request.POST['title'])
            response = []
            for i in range(0, len(serie_id)):
                serie = api.get_serie_name(serie_id[i])
                response.append(serie)
            context = {'response': response}
            return HttpResponse(template.render(request=request, context=context))
        else:
            raise EnvironmentError
    else:
        form = TVShowForm()
    return render(request, 'LikeSeries/results.html', {'form': form})

# fonction qui récupère l'id/l'objet de la série sur laquelle on a cliqué dans la page results
def TVShowPage(request):
    tv_id = request.GET.get('tv_id')
    from myTVSeries import api_call
    api = api_call.Api_call()
    serie = api.get_serie(tv_id)
    person = api.want_person('tv_id')
    context = {'serie': serie, 'person': person}
    template = loader.get_template('LikeSeries/TVShow_page.html')
    return HttpResponse(template.render(request=request, context=context))

# fonction qui permet de liker les séries et de former une base de données à partir de cette action
def Save_like(request):
    if request.method == 'POST':
        like = LikeForm(request.POST)
    else:
        raise EnvironmentError


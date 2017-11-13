# coding=utf-8

from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from .forms import TVShowForm, LikeForm
from django.template import loader
import json

import sys
sys.path.append("..")

import api_call

def home(request):
    return HttpResponse("Bienvenue sur MyTVSeries. Likes les séries que tu aimes!")

# Pour chercher dans la base de données avec le titre de la série, le genre, le réalisateur, les notes etc...

def search(request):
    if request.method == 'POST':
        form = TVShowForm(request.POST)
        if form.is_valid():
            api = api_call.Api_call()
            template = loader.get_template('LikeSeries/results.html')
            serie_id = api.get_tv_id(request.POST['title'])
            response = []
            for i in range(0, len(serie_id)):
                serie = api.get_serie(serie_id[i])
                response.append(serie)
            context = {'response': response}
            return HttpResponse(template.render(request=request, context=context))
        else:
            raise EnvironmentError
    else:
        form = TVShowForm()
    return render(request, 'LikeSeries/index.html', {'form': form})

# fonction qui récupère l'id/l'objet de la série sur laquelle on a cliqué dans la page results
def TVShowPage(request, tv_id):
    api = api_call.Api_call()
    serie = api.get_serie(tv_id)
    actors = api.get_serie_actors(tv_id)
    context = {'serie': serie, 'actors': actors}
    template = loader.get_template('LikeSeries/TVShow_page.html')
    return HttpResponse(template.render(request=request, context=context))

# fonction qui permet de liker les séries et de former une base de données à partir de cette action
def Save_like(request):
    if request.method == 'POST':
        like = LikeForm(request.POST)
    else:
        raise EnvironmentError


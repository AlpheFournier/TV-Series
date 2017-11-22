# coding=utf-8

from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from .forms import TVShowForm, LikeForm
from .models import TVShow, UserLikes
from django.template import loader
import json
from .exception import AuthenticationException

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
    #création de l'objet TVShow pour pouvoir enregistrer les informations propres à cet objet spécifique (par exemple les likes)
    tv_show = TVShow(serie)
    actors = api.get_serie_actors(tv_id)
    context = {'serie': serie, 'actors': actors,'tv_show': tv_show}
    template = loader.get_template('LikeSeries/TVShow_page.html')
    return HttpResponse(template.render(request=request, context=context))

# Page correspondant à une saison d'une série donnée
def Season_Page(request,tv_id,season_number):
    api = api_call.Api_call()
    serie = api.get_serie(tv_id)
    season = api.get_season(tv_id,season_number)
    context = {'serie':serie, 'season':season}
    template = loader.get_template('LikeSeries/Season.html')
    return HttpResponse(template.render(request=request, context=context))

#Page correspondant à un épisode d'une saison d'une série donnée
def Episode_Page(request,tv_id,season_number, episode_number):
    api = api_call.Api_call()
    serie = api.get_serie(tv_id)
    season = api.get_season(tv_id, season_number)
    episode = api.get_episode(tv_id, season_number, episode_number)
    context = {'serie': serie, 'season': season, 'episode': episode}
    template = loader.get_template('LikeSeries/Episode.html')
    return HttpResponse(template.render(request=request, context=context))

#Page pour chaque acteur
def Actor_Page(request, act_id):
    api = api_call.Api_call()
    actor = api.get_person(act_id)
    tv_credits = api.get_tv_credits(act_id)
    context = {'actor':actor, 'tv_credits':tv_credits}
    template = loader.get_template('LikeSeries/Actor.html')
    return HttpResponse(template.render(request=request, context=context))

# fonction qui permet de liker les séries et de former une base de données à partir de cette action
"""def Save_like(request, tv_id):
    likes= UserLikes()
    query_results = UserLikes.objects.filter(user=request.user).all()
    print (query_results)
    for x in query_results :
        if
    likes.user=request.user
    likes.tv_id_liked = tv_id
    #likes.save()
    
    if request.user.is_authenticated():
        likes.user = request.user
        # On utilise un décodeur json pour décoder notre chaine de caractères likes.tv_id_liked
        jsonDec = json.decoder.JSONDecoder()
        # On le transforme en liste avec json
        list_tv_id_liked = jsonDec.decode(likes.tv_id_liked)
        # On rajoute chaque id à cette liste

        ########### attention, je crois que ça marche pas !###################################################
        print(list_tv_id_liked)
        if not tv_id in list_tv_id_liked:
            list_tv_id_liked.append(tv_id)
            # On retransforme la liste modifée en chaine de caractères
            likes.tv_id_liked = json.dumps(list_tv_id_liked)
            likes.save()
    api = api_call.Api_call()
    serie = api.get_serie(tv_id)
    #création de l'objet TVShow pour pouvoir enregistrer les informations propres à cet objet spécifique (par exemple les likes)
    tv_show = TVShow(serie)
    actors = api.get_serie_actors(tv_id)
    context = {'serie': serie, 'actors': actors,'tv_show': tv_show}
    template = loader.get_template('LikeSeries/TVShow_page.html')
    return HttpResponse(template.render(request=request, context=context))"""


def LikeSerie(request, tv_id):
    apic = api_call.Api_call()
    apic.LikeSerie(request.user, tv_id)
    serie = apic.get_serie(tv_id)
    tv_show = TVShow(serie)
    actors = apic.get_serie_actors(tv_id)
    context = {'serie': serie, 'actors': actors,'tv_show': tv_show}
    template = loader.get_template('LikeSeries/TVShow_page.html')
    return HttpResponse(template.render(request=request, context=context))



def Afficher_series_liked(request):
    api = api_call.Api_call()
    query_results = UserLikes.objects.filter(user=request.user).all()
    for x in query_results :
        print (x.user)
        print (x.tv_id_liked)
    serie_liked = []
    id_liked = []
    for x in query_results:
        list_tv_id_liked = x.tv_id_liked
        print(list_tv_id_liked)
        id_liked.append(list_tv_id_liked)
    for x in id_liked:
        serie_liked.append(api.get_serie(x))
    if request.user.is_authenticated():
        context = {'serie_liked': serie_liked}
        template = loader.get_template('LikeSeries/Bibliotheque.html')
        return HttpResponse(template.render(request=request, context=context))


def RemoveLike(request, tv_id) :
    apic = api_call.Api_call()
    apic.RemoveLike(request.user, tv_id)
    return Afficher_series_liked(request)

# coding=utf-8
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from .forms import TVShowForm
from .models import TVShow, UserLikes
from django.template import loader
import sys
import api_call
sys.path.append("..")

# Pour chercher dans la base de donnees avec le titre de la serie
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

#Fonction pour liker une serie
def LikeSerie(request, tv_id):
    apic = api_call.Api_call()
    apic.LikeSerie(request.user, tv_id)
    serie = apic.get_serie(tv_id)
    tv_show = TVShow(serie)
    actors = apic.get_serie_actors(tv_id)
    context = {'serie': serie, 'actors': actors,'tv_show': tv_show}
    template = loader.get_template('LikeSeries/TVShow_page.html')
    return HttpResponse(template.render(request=request, context=context))

#Fonction pour afficher les series
def Afficher_series_liked(request):
    api = api_call.Api_call()
    query_results = UserLikes.objects.filter(user=request.user).all()
    serie_liked = []
    next_episodes = []
    id_liked = []
    for x in query_results:
        list_tv_id_liked = x.tv_id_liked
        if list_tv_id_liked not in id_liked :
            id_liked.append(list_tv_id_liked)
    for x in id_liked:
        serie_liked.append(api.get_serie(x))
        next_episodes.append(api.next_episodes(x))
    if request.user.is_authenticated():
        context = {'serie_liked': serie_liked, 'next_episodes':next_episodes}
        template = loader.get_template('LikeSeries/Bibliotheque.html')
        return HttpResponse(template.render(request=request, context=context))
    
#Fonction pour supprimer une serie
def RemoveLike(request, tv_id) :
    apic = api_call.Api_call()
    apic.RemoveLike(request.user, tv_id)
    return Afficher_series_liked(request)

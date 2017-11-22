import requests
from datetime import datetime

class Api_call:
    url = "https://api.themoviedb.org/3/"
    api_key = "?api_key=52d6a72d6078ec54905fb65e4c55c301"

    def __init__(self):
        pass

    def get_tv_id(self,query):
        resp = requests.get(Api_call.url + "search/tv" + Api_call.api_key + "&query=" + query)
        answer = []
        for item in resp.json()['results']:
            answer.append(item['id'])
        return answer

# On recupere toutes les donnees de la serie sous forme d'un dictionnaire json:
    def get_serie(self,query):
        resp = requests.get(Api_call.url + "tv/" + str(query) + Api_call.api_key)
        serie = resp.json()
        return serie

    def get_serie_actors(self, query):
        resp = requests.get(Api_call.url + "tv/" + str(query) + "/credits" + Api_call.api_key)
        actor = resp.json()['cast']
        return actor

    def get_season(self, query, don):
        resp = requests.get(Api_call.url + "tv/" + str(query) + "/season/" + str(don) + Api_call.api_key)
        season = resp.json()
        return season

    def get_episode(self, query, don, quete):
        resp = requests.get(Api_call.url + "tv/" + str(query) + "/season/" + str(don) + "/episode/" + str(quete) + Api_call.api_key)
        episode = resp.json()
        return episode

    def get_person_id(self, query):
        resp = requests.get(Api_call.url + "search/person" + Api_call.api_key + "&query=" + query)
        answer = []
        for item in resp.json()['results']:
            answer.append(item['id'])
        return answer

    def get_person(self,query):
        resp = requests.get(Api_call.url + "person/" + str(query) + Api_call.api_key)
        actor = resp.json()
        return actor

    def get_tv_credits(self,query):
        resp = requests.get(Api_call.url + "person/" + str(query) + "/tv_credits" + Api_call.api_key)
        tv_credits = resp.json()['cast']
        print(tv_credits)
        return tv_credits

    def want_picture(self, query):
        resp = requests.get(Api_call.url + "tv/" + str(query) + "/images" + Api_call.api_key)
        ans = resp.json()
        image = ans.get('backdrops')[0].get('file_path')
        url_image = "https://image.tmdb.org/t/p/w640" + image
        return(url_image)

    def discover_serie(self):
        resp = requests.get (Api_call.url + "discover/tv/" + Api_call.api_key + "&sor_by=vote_average.desc&page=1&include_null_first_air_dates=false'")
        ans = requests.get(resp)
        answer = []
        for element in ans.json()['results']:
            answer.append(element['name'])
        print("The {} highest rated series are: ".format(len(answer)))
        return answer

    def next_episodes(self, tv_id, list):
        list_id = list
        while len(list_id) != 0:
            resp = requests.get(Api_call.url + "tv/" + str(tv_id) + Api_call.api_key)
            serie = resp.json()
            last_season = 1
            # On va chercher la dernière saison existante
            for item in serie.seasons :
                last_season = item.season_number
            resp = requests.get(Api_call.url + "tv/" + str(tv_id) + "/season/" + str(last_season) + Api_call.api_key)
            season = resp.json()
            today = datetime.now()
            if season['air date'] == None:
                return {tv_id: {}}
            date_first_episode = datetime.strptime(season['air_date'], "%Y-%m-%d")
            result = []
            if (today - date_first_episode).days > 0 and (today - date_first_episode).days < 365:
                for episode in season['episodes']:
                    date_episode = datetime.strptime(episode['air_date'], "%Y-%m-%d")
                    if date_episode > today:
                        if (date_episode - today).days <= 7:
                            return {tv_id: episode}
            else:
                list_id = list_id[1:]
        return {tv_id: {}}

    def infos_next_episodes(self, series_list):
        result = []
        for series in series_list:
            list_season = []
            episode = {}
            if series['status'] == 'Returning Series':
                if len(series['seasons']) == 1:
                    list_season = [0]
                else:
                    list_season = [0] * (len(series['seasons']) - 1)
                episode = self.next_episodes(series['id'], list_season)
                if episode[series['id']] == {}:
                    if series['networks'] != [] and series['networks'][0].get['name'] == 'Netflix':
                        series.is_netflix = True
                    else:
                        series.is_netflix = False
                    series.is_coming_soon = False
                else:
                    series.is_coming_soon = True
                    series.episode_coming_soon_name = episode[series.id]['name']
                    series.episode_coming_soon_air_date = episode[series.id]['air_date']
            else:
                series.is_coming_soon = False
            result.append(series)
        return result

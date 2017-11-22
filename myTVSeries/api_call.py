import requests
from datetime import datetime
from LikeSeries.models import UserLikes

class Api_call:
    url = "https://api.themoviedb.org/3/"
    api_key = "?api_key=52d6a72d6078ec54905fb65e4c55c301"

    def __init__(self):
        pass

    def get_tv_id(self,query):
        """
        :param query: Corresponding to the search of the user
        :return: Returns a list of the series' ids
        """
        resp = requests.get(Api_call.url + "search/tv" + Api_call.api_key + "&query=" + query)
        answer = []
        for item in resp.json()['results']:
            answer.append(item['id'])
        return answer

# On recupere toutes les donnees de la serie sous forme d'un dictionnaire json:
    def get_serie(self,query):
        """
        :param query: Serie's id
        :return: Returns the serie corresponding to the id
        """
        resp = requests.get(Api_call.url + "tv/" + str(query) + Api_call.api_key)
        serie = resp.json()
        return serie

    def get_serie_actors(self, query):
        """
        :param query: Serie's id
        :return: Returns an actors' list corresponding to the serie's id
        """
        resp = requests.get(Api_call.url + "tv/" + str(query) + "/credits" + Api_call.api_key)
        actor = resp.json()['cast']
        return actor

    def get_season(self, query, don):
        """
        :param query: Serie's id
        :param don: Season's number of the serie
        :return: Returns the season corresponding to the serie's id and its number
        """
        resp = requests.get(Api_call.url + "tv/" + str(query) + "/season/" + str(don) + Api_call.api_key)
        season = resp.json()
        return season

    def get_episode(self, query, don, quete):
        """
        :param query: Serie's id
        :param don: Season's number of the serie
        :param quete: Episode's number of the season
        :return: Returns the episode corresponding to the serie's id, its season's number ans its episode's number
        """
        resp = requests.get(Api_call.url + "tv/" + str(query) + "/season/" + str(don) + "/episode/" + str(quete) + Api_call.api_key)
        episode = resp.json()
        return episode

    def get_person_id(self, query):
        """
        :param query: Corresponding to the search of the user
        :return: Returns a list of the person' ids
        """
        resp = requests.get(Api_call.url + "search/person" + Api_call.api_key + "&query=" + query)
        answer = []
        for item in resp.json()['results']:
            answer.append(item['id'])
        return answer

    def get_person(self,query):
        """
        :param query: Person's id
        :return: Returns a person
        """
        resp = requests.get(Api_call.url + "person/" + str(query) + Api_call.api_key)
        actor = resp.json()
        return actor

    def get_tv_credits(self,query):
        """
        :param query: Person's id
        :return: Returns a list of the person's series
        """
        resp = requests.get(Api_call.url + "person/" + str(query) + "/tv_credits" + Api_call.api_key)
        tv_credits = resp.json()['cast']
        print(tv_credits)
        return tv_credits

    def want_picture(self, query):
        """
        :param query: Serie's id
        :return: Returns a picture of the serie
        """
        resp = requests.get(Api_call.url + "tv/" + str(query) + "/images" + Api_call.api_key)
        ans = resp.json()
        image = ans.get('backdrops')[0].get('file_path')
        url_image = "https://image.tmdb.org/t/p/w640" + image
        return(url_image)

    def discover_serie(self):
        """
        :return: Returns the twenty best series
        """
        resp = requests.get (Api_call.url + "discover/tv/" + Api_call.api_key + "&sor_by=vote_average.desc&page=1&include_null_first_air_dates=false'")
        ans = requests.get(resp)
        answer = []
        for element in ans.json()['results']:
            answer.append(element['name'])
        print("The {} highest rated series are: ".format(len(answer)))
        return answer

    def next_episodes(self, tv_id):
        """
        :param tv_id:
        :return: Dictionnary with tv_id and the next episode, if the next episode will be broadcast in less than 7 days, according the API
        """
        resp = requests.get(Api_call.url + "tv/" + str(tv_id) + Api_call.api_key)
        serie = resp.json()
        last_season = 1
        # On va chercher la derniere saison existante
        for item in serie['seasons']:
            last_season = item['season_number']
        resp = requests.get(Api_call.url + "tv/" + str(tv_id) + "/season/" + str(last_season) + Api_call.api_key)
        season = resp.json()
        today = datetime.now()
        if season['air_date'] == None:
            dict = {}
            dict['tv_id'] = tv_id
            return dict
        date_first_episode = datetime.strptime(season['air_date'], "%Y-%m-%d")
        if (date_first_episode - today).days > 0:
            dict = season['episodes'][0]
            dict['tv_id'] = tv_id
            return dict
        elif (date_first_episode - today).days < 0:
            for episode in season['episodes']:
                try :
                    date_episode = datetime.strptime(episode['air_date'], "%Y-%m-%d")
                except :
                    dict = {}
                    dict['tv_id'] = tv_id
                    return dict
                if date_episode > today:
                    if (date_episode - today).days <= 7:
                        dict = episode
                        dict['tv_id'] = tv_id
                        return dict
        dict = {}
        dict['tv_id'] = tv_id
        return dict



    def LikeSerie(self, user, tv_id):
        """
        :param user: Current user
        :param tv_id: Serie's id
        :return: Save in the data base a new object UserLikes
        """
        newEntry=UserLikes(user=user,tv_id_liked=tv_id)
        newEntry.save()
        return 'OK'


    def RemoveLike(self, user, tv_id):
        """
        :param user: Current user
        :param tv_id: Serie's id
        :return: Remove in the data base the object UserLikes
        """
        UserLikes.objects.filter(user_id=user.id,tv_id_liked=tv_id).delete()
        return 'OK'

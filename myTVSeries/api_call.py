import requests

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

    def get_serie(self,query):
        resp = requests.get(Api_call.url + "tv/" + str(query) + Api_call.api_key)
        serie = resp.json()
        return serie

    def get_serie_actors(self, query):
        resp = requests.get(Api_call.url + "tv/" + str(query) + "/credits" + Api_call.api_key)
        actor = resp.json()['cast']
        return actor

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

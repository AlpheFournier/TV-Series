import requests
from myTVSeries.LikeSeries.models import TVShow

class Api_call:
    url = "https://api.themoviedb.org/3/"
    api_key = "?api_key=52d6a72d6078ec54905fb65e4c55c301"

    def __int__(self):
        pass

    def want_serie(self, query):
        resp = requests.get(Api_call.url + "search/tv" + Api_call.api_key + "&query" + query)
        answer = []
        for element in resp.json()['answer']:
            x = TVShow(element)
            answer.append(x)
        return answer

    def get_tv_id(self,query):
        resp = requests.get(Api_call.url + "search/tv" + Api_call.api_key + "&query" + query)
        answer = []
        for element in resp.json()['answer']:
            answer.append(element['id'])
        return answer

    def want_person(self, query):
        resp = requests.get(Api_call.url + "search/person" + Api_call.api_key + "&query" + query)
        answer = []
        for element in resp.json()['answer']:
            answer.append(element['name'])
        return answer

    def want_picture(self):
        # We use id=1399, it corresponds to Game of thrones, and we can't use a random because there is some series which doesn't have any associated picture...
        resp = requests.get(Api_call.url + "tv/1399/images" + Api_call.api_key)
        ans = resp.json()
        image = ans.get('backdrops')[0].get('file_path')
        url_image = "https://image.tmdb.org/t/p/w640" + image
        return(url_image)

    def element_serie(self, id):
        resp = requests.get(Api_call.url + "tv/" + str(id) + Api_call.api_key)
        answer = []
        for element in resp.json()['answer']:
            answer.append(element)
        return answer

    def discover_serie(self):
        resp = requests.get (Api_call.url + "discover/tv/" + Api_call.api_key + "&sor_by=vote_average.desc&page=1&include_null_first_air_dates=false'")
        ans = requests.get(resp)
        answer = []
        for element in ans.json()['answer']:
            answer.append(element['name'])
        print("The {} highest rated series are: ".format(len(answer)))
        return answer
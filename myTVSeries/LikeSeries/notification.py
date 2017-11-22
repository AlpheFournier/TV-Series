import requests
from .models import TVShow, User_Likes
import json

import sys
sys.path.append("..")
import api_call

def link_user_episode(self):
    result =[]
    api = api_call.Api_call()
    jsonDec = json.decoder.JSONDecoder()
    query_results = User_Likes.objects.all()
    serie_liked = []
    id_liked = []
    for x in query_results:
        list_tv_id_liked = jsonDec.decode(x.tv_id_liked)
        for y in list_tv_id_liked:
            id_liked.append(y)
    for x in set(id_liked):
        serie_liked.append(api.get_serie(x))
    for serie in serie_liked:
        list = []
        episode = {}


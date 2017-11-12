from django.db import models

class TVShow():

    def __init__(self,dico):
        for i,j in dico.items():
            setattr(self,i,j)

    @property
    def tv_id(self):
        return self.tv_id

    @property
    def name(self):
        return self.name

    @property
    def language(self):
        return self.language

    @property
    def overview(self):
        return self.overview

    @property
    def gender(self):
        return self.gender

    @property
    def vote_avg(self):
        return self.vote_avg

    @property
    def director(self):
        return self.director

    @tv_id.setter
    def tv_id(self, value):
        self._tv_id = value

    @name.setter
    def name(self, value):
        self._name = value

    @language.setter
    def language(self, value):
        self._language = value

    @overview.setter
    def overview(self, value):
        self._overview = value

    @gender.setter
    def gender(self, value):
        self._gender = value

    @vote_avg.setter
    def vote_avg(self, value):
        self._vote_avg = value

    @director.setter
    def director(self, value):
        self.director = value

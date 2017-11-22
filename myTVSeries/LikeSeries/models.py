from django.db import models
from django.contrib.auth.models import User

class UserLikes(models.Model):
    user = models.ForeignKey(User)
    tv_id_liked = models.CharField(max_length=100)


class TVShow(models.Model):
    tv_id = models.IntegerField()
    title = models.CharField(max_length=200, blank=False)
    director = models.CharField(max_length=200, blank=True)
    language = models.CharField(max_length=20, blank=True)
    actors = models.CharField(max_length=200, blank=True)
    overview = models.CharField(max_length=30)
    gender = models.CharField(max_length=10, blank=True)
    vote_avg = models.IntegerField()


class Person(models.Model):

    def __init__(self,dic):
        super(Person, self).__init__()
        for i,j in dic.items():
            setattr(self,i,j)

    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    birthday = models.DateField()
    deathday = models.DateField()
    biography = models.CharField(max_length=2000)
    mark = models.IntegerField()

    @property
    def name(self):
        return self.name

    @property
    def gender(self):
        return self.gender

    @property
    def birthday(self):
        return self.birthday

    @property
    def deathday(self):
        return self.deathday

    @property
    def biography(self):
        return self.biography

    @property
    def mark(self):
        return self.mark

    @name.setter
    def name(self, value):
        self._name = value

    @gender.setter
    def gender(self, value):
        self._gender = value

    @birthday.setter
    def birthday(self, value):
        self._birthday = value

    @deathday.setter
    def deathday(self, value):
        self._deathday = value

    @biography.setter
    def biography(self, value):
        self._biography = value

    @mark.setter
    def mark(self, value):
        self._mark = value





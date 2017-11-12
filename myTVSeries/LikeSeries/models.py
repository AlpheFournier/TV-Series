from django.db import models

# Create your models here.

class TVShow(models.Model):

    GENRE_OPTIONS = (
        ('Horror', 'Horror'),
        ('Drama', 'Drama'),
        ('Comedy', 'Comedy'),
        ('SciFi', 'SciFi'),
        ('Action', 'Action'),
        ('Period', 'Period')
    )

    tv_id = models.IntegerField()
    title = models.CharField(max_length=200)
    director = models.CharField(max_length=200, blank=True)
    language = models.CharField(max_length=20, blank=True)
    actors = models.CharField(max_length=200, blank=True)
    overview = models.CharField(max_length=30)
    gender = models.CharField(max_length=10,
                              choices=GENRE_OPTIONS, blank=True)
    vote_avg = models.IntegerField()


"""
#Nos accesseurs

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
      self.director = value """

class Person():

    def __init__(self,dic):
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

class Like (models.Model):
    like_counter = models.IntegerField()




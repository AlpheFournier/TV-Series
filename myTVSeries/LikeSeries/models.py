from django.db import models
from django.contrib import admin

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
    language = models.CharField(max_length=20)
    director = models.CharField(max_length=30)
    genre = models.CharField(max_length=10,
                             choices=GENRE_OPTIONS)
    mark= models.IntegerField()

    #Nos accesseurs

    @property
    def tv_id(self):
        return self.tv_id

    @property
    def title(self):
        return self.title

    @property
    def language(self):
        return self.language

    @property
    def director(self):
        return self.director

    @property
    def genre(self):
        return self.genre

    @property
    def mark(self):
        return self.mark

    @tv_id.setter
    def tv_id(self, value):
        self._tv_id = value

    @title.setter
    def title(self, value):
        self._title = value

    @language.setter
    def language(self, value):
        self._language = value

    @director.setter
    def director(self, value):
        self._director = value

    @genre.setter
    def genre(self, value):
        self._genre = value

    @mark.setter
    def mark(self, value):
        self._mark = value


class Person(models.Model):

    last_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    birthday = models.DateField()
    deathday = models.DateField()
    biography = models.CharField(max_length=2000)
    mark = models.IntegerField()

    @property
    def last_name(self):
        return self.last_name

    @property
    def first_name(self):
        return self.first_name

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

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

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


class ItemAdmin(admin.ModelAdmin):
    list_display = ["title"]
    search_fields = ["title"]

admin.site.register(TVShow, ItemAdmin)








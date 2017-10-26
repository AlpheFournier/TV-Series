from django.db import models
from django.contrib import admin

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class TVShow(models.Model):

    GENRE_OPTIONS = (
        ('Horror', 'Horror'),
        ('Drama', 'Drama'),
        ('Comedy', 'Comedy'),
        ('SciFi', 'SciFi'),
        ('Action', 'Action'),
        ('Period', 'Period')
    )
    title = models.CharField(max_length=200)
    language = models.CharField(max_length=20)
    director = models.CharField(max_length=30)
    genre = models.CharField(max_length=10,
                             choices=GENRE_OPTIONS)
    mark= models.IntegerField()


class ItemAdmin(admin.ModelAdmin):
    list_display = ["title"]
    search_fields = ["title"]

admin.site.register(TVShow, ItemAdmin)








from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader

def welcome(request):
    return HttpResponse("Bienvenue sur MyTVSeries. Likes les séries que tu aimes!")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def like(request, question_id):
    return HttpResponse("You're liking on question %s." % question_id)

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('LikeSeries/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
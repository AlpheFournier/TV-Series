from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from .models import Choice, Question, TVShow
from django.urls import reverse
from django.views import generic
from .forms import TVShowForm

def home(request):
    return HttpResponse("Bienvenue sur MyTVSeries. Likes les séries que tu aimes!")

def like(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'LikeSeries/detail.html', {
            'question': question,
        })
    else:
        selected_choice.likes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('LikeSeries:results', args=(question.id,)))


class IndexView(generic.ListView):
    template_name = 'LikeSeries/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'LikeSeries/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'LikeSeries/results.html'

def add_TVShow_form(request):
    if request.POST:
        form = TVShowForm(request.POST)
        if form.is_valid():
            # On vérifie que la série existe déjà dans la base de données
            check_db = TVShow.objects.filter(title=request.POST['title'])
            if len(check_db) > 0:
                # If a movie with same name exists the do not enter to DB
                return render(request, 'TVShow_exists.html',
                              {'TVShow_title': request.POST['title']})
            else:
                # Save form and redirect to the success page
                form.save()
                return render_to_response('add_success.html',
                                          {'TVShow_title': request.POST['title']})
    else:
        form = TVShowForm()
    return render(request, 'add_TVShow_form.html',
                  {'form': form})

def search(request):
    # Pour chercher dans la base de données avec le titre de la série, le genre, le réalisateur, les notes etc...
    if request.GET:
        TVShow_listing = []
        search_string = ""
        if request.GET['title']:
            for TVShow_object in TVShow.objects.filter(title__contains=request.GET['title']):
                TVShow_dict = {'TVShow_object': TVShow_object}
                TVShow_listing.append(TVShow_dict)
            search_string = request.GET['title']
        if request.GET['genre']:
            for TVShow_object in TVShow.objects.filter(genre__contains=request.GET['genre']):
                TVShow_dict = {'TVShow_object': TVShow_object}
                TVShow_listing.append(TVShow_dict)
            search_string = " ".join((search_string, request.GET['genre']))
        if request.GET['director']:
            for TVShow_object in TVShow.objects.filter(director__contains=request.GET['director']):
                TVShow_dict = {'TVShow_object': TVShow_object}
                TVShow_listing.append(TVShow_dict)
            search_string = " ".join((search_string, request.GET['director']))
        if request.GET['language']:
            for TVShow_object in TVShow.objects.filter(language__contains=request.GET['language']):
                TVShow_dict = {'TVShow_object': TVShow_object}
                TVShow_listing.append(TVShow_dict)
            search_string = " ".join((search_string, request.GET['language']))
        if request.GET['mark']:
            for TVShow_object in TVShow.objects.filter(mark__contains=request.GET['mark']):
                TVShow_dict = {'TVShow_object': TVShow_object}
                TVShow_listing.append(TVShow_dict)
            search_string = " ".join((search_string, request.GET['mark']))
        if len(TVShow_listing) > 0:
            return render_to_response('results.html', {'search_string': search_string,
                                                       'TVShow_listing': TVShow_listing})
    form = TVShowForm()
    return render(request,'index.html', {'form': form})





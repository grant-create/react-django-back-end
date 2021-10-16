from django.shortcuts import render
from django.http import HttpResponse
from movies.config import api_key

# Create your views here.

def index(request):
    return HttpResponse("hello, you're in the movie index")

def home(request):
    response = request.get(f'http://www.omdbapi.com/?i=tt3896198&apikey={api_key}')
    moviedata = response.json()
    return render(request)
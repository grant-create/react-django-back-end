from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from movies.config import api_key
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

# import the model and serializer and return it as JSON response
from movies.models import Movie
from movies.serializers import MovieSerializer


# Create your views here.

def index(request):
    return HttpResponse("hello, you're in the movie index")

# def home(request):
#     response = request.get(f'http://www.omdbapi.com/?i=tt3896198&apikey={api_key}')
#     moviedata = response.json()
#     return render(request)

def test(request):
    if request.method=='GET':
        return JsonResponse(MovieSerializer.data, safe=False)


    elif request.method=='POST':

        new_data=JSONParser().parse(request)
        new_movie_serializer=MovieSerializer(data=new_data)
        if new_movie_serializer.is_valid():
            new_movie_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
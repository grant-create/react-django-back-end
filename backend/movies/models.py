from typing_extensions import runtime
from django.db import models

# Create your models here.


#  Will likely need to update this model to just be a movie list,
#  instead of a user with movie list
# will need to check django docs to remigrate models If I can ever get them to react


# ref: https://www.youtube.com/watch?v=Uyei2iDA4Hs @ 9:00

# thinking of adding a user model to let each user have their own favorites.

class Movie(models.Model):
    # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250)
    runtime = models.CharField(max_length=200, blank=True)
    image = models.CharField(max_length=500, blank=True)
    

    # need to: python3 manage.py makemigrations movies
    # then, python3 manage.py migrate



# class Watchlist(models.Model):
#     watch_list = models.ForeignKey(Movie, on_delete=models.CASCADE)

# class Seen(models.Model):
#     watched = models.ForeignKey(Movie, on_delete=models.CASCADE)
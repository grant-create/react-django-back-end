from django.db import models

# Create your models here.


#  Will likely need to update this model to just be a movie list,
#  instead of a user with movie list
# will need to check django docs to remigrate models If I can ever get them to react

class Movie(models.Model):
    name = models.CharField(max_length=25, unique=True)
    password = models.CharField(max_length=100)
    
    

# class Watchlist(models.Model):
#     watch_list = models.ForeignKey(Movie, on_delete=models.CASCADE)

# class Seen(models.Model):
#     watched = models.ForeignKey(Movie, on_delete=models.CASCADE)
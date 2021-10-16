from django.db import models

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=25, unique=True)
    password = models.CharField(max_length=100)
    
    

class Watchlist(models.Model):
    watch_list = models.ForeignKey(Movie, on_delete=models.CASCADE)

class Seen(models.Model):
    watched = models.ForeignKey(Movie, on_delete=models.CASCADE)
from django.db import models

# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.PositiveIntegerField()
    genres = models.ManyToManyField(Genre)
    actors = models.ManyToManyField('Actor')
    directors = models.ManyToManyField('Director')
    producers = models.ManyToManyField('Producer')

    def __str__(self):
        return self.title

class Actor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Producer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

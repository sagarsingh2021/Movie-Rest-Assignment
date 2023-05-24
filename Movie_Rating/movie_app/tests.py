from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Genre, Movie, Actor, Director, Producer
from .serializers import MovieSerializer, GenreSerializer

class MovieAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Create test data
        self.genre1 = Genre.objects.create(name='Drama')
        self.genre2 = Genre.objects.create(name='Comedy')

        self.actor1 = Actor.objects.create(name='Shah Rukh Khan')
        self.actor2 = Actor.objects.create(name='Deepika Padukone')

        self.director1 = Director.objects.create(name='Karan Johar')
        self.director2 = Director.objects.create(name='Rohit Shetty')

        self.producer1 = Producer.objects.create(name='Yash Raj Films')
        self.producer2 = Producer.objects.create(name='Dharma Productions')

        self.movie1 = Movie.objects.create(title='KKGM', release_year=2021)
        self.movie1.genres.set([self.genre1, self.genre2])
        self.movie1.actors.set([self.actor1, self.actor2])
        self.movie1.directors.set([self.director1, self.director2])
        self.movie1.producers.set([self.producer1, self.producer2])

        self.movie2 = Movie.objects.create(title='CHEN', release_year=2013)
        self.movie2.genres.set([self.genre2])
        self.movie2.actors.set([self.actor2])
        self.movie2.directors.set([self.director2])
        self.movie2.producers.set([self.producer2])

    def test_get_all_movies(self):
        response = self.client.get('/movies/')
        movies = Movie.objects.all()
        serializer_data = MovieSerializer(movies, many=True).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer_data)

    def test_create_movie(self):
        data = {
            'title': 'Dilwale',
            'release_year': 2015,
            'genres': [self.genre1.id],
            'actors': [self.actor1.id],
            'directors': [self.director1.id],
            'producers': [self.producer1.id]
        }
        response = self.client.post('/movies/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], data['title'])
        self.assertEqual(response.data['release_year'], data['release_year'])
        self.assertEqual(response.data['genres'], [self.genre1.id])
        self.assertEqual(response.data['actors'], [self.actor1.id])
        self.assertEqual(response.data['directors'], [self.director1.id])
        self.assertEqual(response.data['producers'], [self.producer1.id])

    def test_update_movie(self):
        data = {
            'title': 'Dil Chahta Hai',
            'release_year': 2001,
            'genres': [self.genre2.id],
            'actors': [self.actor2.id],
            'directors': [self.director2.id],
            'producers': [self.producer2.id]
        }
        response = self.client.put(f'/movies/{self.movie1.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], data['title'])
        self.assertEqual(response.data['release_year'], data['release_year'])
        self.assertEqual(response.data['genres'], [self.genre2.id])
        self.assertEqual(response.data['actors'], [self.actor2.id])
        self.assertEqual(response.data['directors'], [self.director2.id])
        self.assertEqual(response.data['producers'], [self.producer2.id])

    def test_delete_movie(self):
        response = self.client.delete(f'/movies/{self.movie1.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Movie.objects.filter(id=self.movie1.id).exists())

    def test_get_all_genres(self):
        response = self.client.get('/genres/')
        genres = Genre.objects.all()
        serializer_data = GenreSerializer(genres, many=True).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer_data)


    def test_get_single_movie(self):
        response = self.client.get(f'/movies/{self.movie1.id}/')
        movie = Movie.objects.get(id=self.movie1.id)
        serializer_data = MovieSerializer(movie).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer_data)


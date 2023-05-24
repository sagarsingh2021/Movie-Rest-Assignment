from django.urls import include, path
from rest_framework import routers
from movie_app.views import GenreViewSet, MovieViewSet, ActorViewSet, DirectorViewSet, ProducerViewSet

router = routers.DefaultRouter()
router.register(r'genres', GenreViewSet)
router.register(r'movies', MovieViewSet)
router.register(r'actors', ActorViewSet)
router.register(r'directors', DirectorViewSet)
router.register(r'producers', ProducerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

from rest_framework import routers
from .api import MovieViewSet
from django.urls import path

from . import views

router = routers.DefaultRouter()
router.register('api/movies', MovieViewSet, 'movies')
router.register('', MovieViewSet, 'movies')

urlpatterns = router.urls

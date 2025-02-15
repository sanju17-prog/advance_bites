from django.urls import path, include
from rest_framework import routers
from.views import SingerViewSet, SongViewSet

router = routers.DefaultRouter()
router.register('singers', SingerViewSet, basename='singer')
router.register('songs', SongViewSet, basename='song')

urlpatterns = [
    path('', include(router.urls)),
]

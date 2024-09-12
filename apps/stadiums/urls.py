from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.stadiums import viewsets, views

app_name = 'stadiums'


router = DefaultRouter()
router.register("stadiums", viewsets.StadiumViewSet, basename="stadiums")


urlpatterns = [
    path("search-stadiums/", views.StadiumsListAPI.as_view(), name="search-stadiums"),
] + router.urls
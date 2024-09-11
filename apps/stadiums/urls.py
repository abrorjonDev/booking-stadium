from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.stadiums import views

app_name = 'stadiums'


router = DefaultRouter()
router.register("stadiums", views.StadiumViewSet, basename="stadiums")


urlpatterns = [

] + router.urls
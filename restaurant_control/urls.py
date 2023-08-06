from rest_framework import routers, urlpatterns
from django.urls import path, include
from .views import (
    CreateRestaurantView, UpdateRestaurantView, DeleteRestaurantView, GetAllRestaurantView
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)

router.register("create-restaurant", CreateRestaurantView, 'create restaurant')
router.register("update-restaurant", UpdateRestaurantView, 'update restaurant')
router.register("delete-restaurant", DeleteRestaurantView, 'delete restaurant')
router.register("list-restaurants", GetAllRestaurantView, 'list restaurants')




urlpatterns = [
    path("", include(router.urls)),
]
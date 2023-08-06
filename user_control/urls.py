from rest_framework import routers, urlpatterns
from django.urls import path, include
from .views import (
    CreateUserView, LoginView, UpdatePasswordView, DeleteUserView
)
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


router = DefaultRouter(trailing_slash=False)

router.register("create-user", CreateUserView, 'create user')
router.register("login", LoginView, 'login user')
router.register("update-password", UpdatePasswordView, 'update password')
router.register("delete-user", DeleteUserView, 'delete user')

urlpatterns = [
    path("", include(router.urls)),
    path('jwt/create/', TokenObtainPairView.as_view(), name='jwt-create'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='token-verify'),
]
 
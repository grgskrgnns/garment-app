from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .viewsets import ContactViewSet

router = DefaultRouter()
router.register(r'', ContactViewSet)
urlpatterns = router.urls
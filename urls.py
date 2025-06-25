from django.urls import path, include
from rest_framework import routers
from .views import UsuarioViewSet  # Agrega tus otros ViewSets aquí

router = routers.DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


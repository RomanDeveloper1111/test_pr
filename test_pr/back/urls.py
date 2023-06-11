from rest_framework import routers
from django.urls import path, include
from back.views import ViewUniqueProducer

router = routers.SimpleRouter()

router.register(r'contract', ViewUniqueProducer, basename='contract')


urlpatterns = [
    path(r'', include(router.urls)),
]
from django.urls import path

from .consumers import WSConsumer


ws_urlpatterns = [
    path('ws/rooms/', WSConsumer.as_asgi())
]
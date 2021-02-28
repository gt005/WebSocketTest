from django.urls import path, include
from .views import *

urlpatterns = [
    path('', MainView.as_view()),
    path('room/<str:room_name>/', RoomView.as_view())
]
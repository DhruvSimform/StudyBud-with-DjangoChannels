from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name='api_routes'),
    path('rooms/', views.getRooms, name='api_rooms'),
    path('rooms/<str:pk>', views.getRoom, name='api_room'),
]
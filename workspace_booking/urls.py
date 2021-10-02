from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_rooms, name='offices'),
    path('add-room/', views.AddRoom.as_view(), name='add-office'),
    path('room-details/<int:pk>', views.room_details, name='room-details'),
]
from django.urls import path 
from . import views


urlpatterns = [
    path('music/', views.SongList.as_view()),
    path('detail/<int:pk>', views.SongDetails.as_view()),
]

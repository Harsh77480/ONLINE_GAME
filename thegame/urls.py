# mysite/urls.py
from django.conf.urls import include
from django.urls import path
from django.contrib import admin

from game import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('createRoom', views.createRoom, name='createRoom'),
    path('joinRoom/<str:code>', views.joinRoom, name='joinRoom'),
    path('gameWaiting/<str:p_name>', views.gameWaiting, name='gameWaiting'),
    path('game_On/<str:room_name>/<str:p_name>', views.gameOn, name='gameOn'),
    path('endGame/<str:p_name>', views.endGame, name='endGame'),
    path('error', views.Error, name='error'),

]
    # path('<str:room_name>/<str:p_name>/', views.room, name='room'),
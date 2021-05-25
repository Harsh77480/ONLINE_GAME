
# chat/routing.py
from django.urls import re_path
from django.urls import include, path
from . import consumers

# from . import consumers

websocket_urlpatterns = [
    # re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
    # path('ws/chat/<str:room_name>/', consumers.ChatConsumer.as_asgi()),
    

    path('ws/game_waiting/<str:room_name>/<str:p_name>/', consumers.game_Waiting.as_asgi()),
    path('ws/game_On/<str:room_name>/<str:p_name>/', consumers.Game_On.as_asgi()),
]
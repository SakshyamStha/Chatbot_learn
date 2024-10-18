from django.urls import path
from . import views

urlpatterns = [
    path('chatbot/', views.chatbot_response, name='chatbot_response'),
    path('chat/', views.chat, name='chat'),  # New path for chat interface
]

from django.urls import path
from . import views

urlpatterns = [
    path('chatbot/chat/', views.chatbot, name='chatbot'),
]

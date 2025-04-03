from django.contrib import admin
from django.urls import path
from api.views.chatbot_views import ChatBotView
from api.views.auth_views import RegisterAPIView

urlpatterns = [
    path('auth/register/', RegisterAPIView.as_view(), name="hello_world"), 
]

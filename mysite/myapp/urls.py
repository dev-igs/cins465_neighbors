from django.urls import path
from django.contrib.auth import views as auth_views
# app level routing/urls

from . import views

urlpatterns = [
    path('', views.index),
    path('login/', auth_views.LoginView.as_view()),
    path('logout/', views.logout_view),
    path('register/', views.register_view),
    path('account/', views.account_view),
    path('chat/', views.chat_view),
    path('chat/<str:room_name>/', views.chatroom_view, name='room'),
    path('events/', views.events_view),
    path('resources/', views.resource_view),
    path('about/', views.about_view),
]
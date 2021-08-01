from django.urls import path
from django.contrib.auth import views as auth_views
# APP LEVEL URL ROUTING

from . import views

urlpatterns = [
    path('',views.index),
    path('feed/',views.feed),
    path('login/', auth_views.LoginView.as_view()),
    path('logout/', views.logout_view),
    path('register/', views.register_view),
    path('auth/signon/',views.signon),
]
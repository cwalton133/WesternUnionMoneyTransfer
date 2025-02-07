from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('send-money/', views.send_money, name='send_money'),
    path('receive-money/', views.receive_money, name='receive_money'),
    path('track-transaction/', views.track_transaction, name='track_transaction'),
]
from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.login, name='login'),
    path('logged_in/', views.logged_in, name='logged_in'),
    path('/message/', views.message_send, name='message'),
]

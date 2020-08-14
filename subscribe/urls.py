from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscribe, name='subscribe'),
    path('home/', views.home, name='home'),
    path('subscribers/', views.subscribers, name='subscribers'),
    path('unsubscribe/', views.unsubscribe, name='unsubscribe')
]

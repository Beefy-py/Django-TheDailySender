from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('subscribers/', views.subscribers, name='subscribers'),
    path('unsubscribe/', views.unsubscribe, name='unsubscribe'),
    path('stay-safe/', views.stay_safe, name='stay_safe')
]

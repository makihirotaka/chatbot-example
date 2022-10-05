
from django.urls import path, include
from api import views

urlpatterns = [
    path('talk/', views.talk, name='talk'),
]

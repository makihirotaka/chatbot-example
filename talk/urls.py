
from django.urls import path, include
from talk import views

urlpatterns = [
    path(r'', views.index, name='index'),
]

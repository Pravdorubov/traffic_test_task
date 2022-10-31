from django.urls import path

from . import views

app_name = 'ttt'
urlpatterns = [
    path('', views.index, name='index'),
]
from django.urls import path

from . import views

app_name = 'olr'
urlpatterns = [
    path('', views.index, name='base')
]

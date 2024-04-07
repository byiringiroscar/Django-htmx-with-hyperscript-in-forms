from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('check_spaces/', views.check_spaces, name='check_spaces')
]
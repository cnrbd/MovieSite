from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'movies.index'),
    path('show/<int:id>/', views.show, name='movies.show')
]
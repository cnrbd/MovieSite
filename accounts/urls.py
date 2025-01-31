from django.urls import path

from home.urls import urlpatterns
from . import views

urlpatterns = [
    path('signup/', views.signup, name= 'signup'),
]
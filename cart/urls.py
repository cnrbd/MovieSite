from django.urls import path
from . import views

app_name = 'cart'
urlpatterns = [
    # path('', views.index, name='cart.index'),
    # path('<int:id>/add/', views.add, name='cart.add'),
    # path('clear/', views.clear, name='cart.clear'),
    # path('purchase/', views.purchase, name='cart.purchase'),

    path('', views.index, name='index'),
    path('<int:id>/add/', views.add, name='add'),
    path('clear/', views.clear, name='clear'),
    path('purchase/', views.purchase, name='purchase'),
]
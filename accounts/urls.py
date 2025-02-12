from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('orders/', views.orders, name='orders'),
    path('changePassword/', views.changePassword, name='changePassword'),
    path('passwordChangeDone/', TemplateView.as_view(template_name='accounts/passwordChangeDone.html'), name='passwordChangeDone'),]
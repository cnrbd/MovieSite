from django.shortcuts import render
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
# from .forms import CustomUserCreationForm, CustomErrorList
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
def signup(request):
    template_data = {}
    template_data['title'] = 'Sign Up'
    if request.method == 'GET':
        template_data['form'] = UserCreationForm()
        return render(request, 'accounts/signup.html',
            {'template_data': template_data})

# def login(request):
#     template_data = {}
#     template_data['title'] = 'Login'
#     if request.method == 'GET':
#         return render(request, 'accounts/login.html', {'template_data': template_data})
#     elif request.method == 'POST':
#         user = authenticate(request, username = request.POST['username'], password = request.POST['password'])
#         if user is None:
#             template_data['error'] = 'The username or password is incorrect.'
#             return render(request, 'accounts/login.html', {'template_data': template_data})
#         else:
#             auth_login(request, user)
#             return redirect('home.index')
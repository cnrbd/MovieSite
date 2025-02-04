from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

#render method takes in:
#1) the HTTP request to be process
#2) the path within the template folder to be rendered

#store app templates under the next directory structure – app_name/templates/app_name/my_template.html.
# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')
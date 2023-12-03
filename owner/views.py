from app.app import auth
from django.shortcuts import render, redirect

# Create your views here.
context = {
    'url': 'Home',
    'title': 'Home',
    'icon': 'static/assets/icon.png'
}
def index(request):
    return render(request, 'owner/index.html', context)
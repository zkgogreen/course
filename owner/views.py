from app.app import auth
from django.shortcuts import render, redirect
from .models import Earn, LevelAkun
from .chart import kelasPie, pendapatan
from user.models import UserMeeting
from django.db.models import Sum
from django.db.models.functions import TruncMonth
import random

# Create your views here.
context = {
    'url': 'Home',
    'title': 'Home',
    'icon': 'static/assets/icon.png'
}
def index(request):
    total_earning = Earn.objects.aggregate(total_earning=Sum('owner'))['total_earning']
    total_earning = total_earning or 0

    

    context['earning'] = total_earning
    context['pendapatan'] =  pendapatan()
    context['pie'] = kelasPie()
    return render(request, 'owner/index.html', context)
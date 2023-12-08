from app.app import auth
from django.shortcuts import render, redirect
from .models import Earn, LevelAkun
from .chart import kelasPie, pendapatan
from user.models import UserMeeting, Users, UserSchadule
from teacher.models import Room
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from django.contrib.auth.models import User as user_root
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

    teacher_list = []
    for teacher in Users.objects.filter(teacher=True):
        teacher = teacher.user
        total_loop = 0
        kuota = 0
        peserta = 0
        for room in Room.objects.filter(mentor=teacher):
            total_loop = total_loop + 1
            kuota = kuota + room.level.people
            peserta = peserta + UserSchadule.objects.filter(room=room).count()
        
        print('total_loop : '+str(total_loop))
        print('kuota : '+str(kuota))
        print('peserta : '+str(peserta))
        teacher.kuota = round((peserta/kuota)*100)

        teacher_list.append(teacher)

    context['pembelian'] = UserMeeting.objects.all()
    context['earning'] = total_earning
    context['pendapatan'] =  pendapatan()
    context['pie'] = kelasPie()
    context['user'] = user_root.objects.filter(is_staff=False, is_superuser=False, is_active=True).count()
    context['teacher'] = teacher_list
    return render(request, 'owner/index.html', context)
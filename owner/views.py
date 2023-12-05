from app.app import auth
from django.shortcuts import render, redirect
from .models import Earn
from django.db.models import Sum
from django.db.models.functions import TruncMonth

# Create your views here.
context = {
    'url': 'Home',
    'title': 'Home',
    'icon': 'static/assets/icon.png'
}
def index(request):
    total_earning = Earn.objects.aggregate(total_earning=Sum('owner'))['total_earning']
    total_earning = total_earning or 0
    earn = Earn.objects.annotate(month=TruncMonth('tgl'))
    bersih_list = earn.values('month').annotate(total_earning=Sum('owner')).order_by('month')
    kotor_list = earn.values('month').annotate(total_earning=Sum('pemasukan')).order_by('month')
    pengeluaran_list = earn.values('month').annotate(total_earning=Sum('pengeluaran')).order_by('month')
    
    context['earning'] = total_earning
    context['bersih'] =  [{'month': monthly_earning['month'].strftime('%Y-%m'), 'total_earning': monthly_earning['total_earning']} for monthly_earning in bersih_list]
    context['kotor'] =  [{'month': monthly_earning['month'].strftime('%Y-%m'), 'total_earning': monthly_earning['total_earning']} for monthly_earning in kotor_list]
    context['pengeluaran'] =  [{'month': monthly_earning['month'].strftime('%Y-%m'), 'total_earning': monthly_earning['total_earning']} for monthly_earning in pengeluaran_list]
    return render(request, 'owner/index.html', context)
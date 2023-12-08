import random
from .models import LevelAkun, Earn
from teacher.models import Withdrow
from user.models import UserMeeting
from django.db.models import Sum
from django.db.models.functions import TruncMonth

def kelasPie():
    level = [{'name': l.name, 'count': UserMeeting.objects.filter(accountlevel=l).count(), 'color': f'#{random.randint(0, 0xFFFFFF):06x}'} for l in LevelAkun.objects.all()]

    dataPie = {
        'labels': [item['name'] for item in level],
        'datasets': [{
            'data': [item['count'] for item in level],
            'backgroundColor': [item['color'] for item in level],
            'hoverOffset': 4,
        }],
    }
    return dataPie

def pendapatan():
    earn = Earn.objects.annotate(month=TruncMonth('tgl'))
    bersih_list_earning = earn.values('month').annotate(total_earning=Sum('owner')).order_by('month')
    simplified_earning = [{'month': monthly_earning['month'].strftime('%Y-%m'), 'total_earning': monthly_earning['total_earning']} for monthly_earning in bersih_list_earning]

    # Fetch 'pengeluaran' data for each month
    bersih_list_pengeluaran = Withdrow.objects.values('tgl').annotate(total_pengeluaran=Sum('jumlah')).order_by('tgl')
    simplified_pengeluaran = [{'month': monthly_pengeluaran['tgl'].strftime('%Y-%m'), 'total_pengeluaran': monthly_pengeluaran['total_pengeluaran']} for monthly_pengeluaran in bersih_list_pengeluaran]

    # Combine 'pendapatan' and 'pengeluaran' data
    dataLineChart = {
        'labels': [item['month'] for item in simplified_earning],
        'datasets': [
            {
                'label': 'Pendapatan',
                'borderColor': '#3498db',
                'data': [item['total_earning'] for item in simplified_earning],
                'fill': 'false',
                'cubicInterpolationMode': 'monotone',
            },
            {
                'label': 'Pengeluaran',
                'borderColor': '#e74c3c',
                'data': [next((item['total_pengeluaran'] for item in simplified_pengeluaran if item['month'] == month), 0) for month in [item['month'] for item in simplified_earning]],
                'fill': 'false',
                'cubicInterpolationMode': 'monotone',
            },
        ],
    }

    return dataLineChart
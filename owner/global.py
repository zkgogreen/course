from .models import Setting

def globalRequest(request):
    return {
        'config':Setting.objects.get()
    }
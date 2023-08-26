from django.http import HttpResponse
from datetime import datetime

# Create your views here. - REQUEST HANDLER

def print_todays_date(request):
    return HttpResponse(datetime.now())
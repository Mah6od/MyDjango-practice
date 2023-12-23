from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Trip, Note

# Create your views here.
class homeview(TemplateView):
    template_name =  'trip/index.html'

def trips_list(request):
    # print(dir(request))
    trips = Trip.objects.filter(owner=request.user)
    context = {
        "trips": trips
    }
    return render(request, 'trip/trips_list.html', context)
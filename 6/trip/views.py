from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class homeview(TemplateView):
    template_name =  'trip/index.html'
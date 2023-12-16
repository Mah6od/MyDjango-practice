from django.shortcuts import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1>job board</h1>')
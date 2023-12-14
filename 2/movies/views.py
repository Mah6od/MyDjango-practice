from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'movies/index.html', {})

def about(request):
    return render(request, 'movies/about.html', {})
from django.shortcuts import HttpResponse, render
from .models import JobPosting


# Create your views here.
def index(request):
    active_posting = JobPosting.objects.filter(is_active= True)
    context = {
        'job_postings': active_posting
    }
    return render(request, 'job_board/index.html', context)

def job_detail(request, pk):
    job_posting = JobPosting.objects.get(pk=pk)
    context = {
        'posting' : job_posting
    }
    return render(request, 'job_board/detail.html', context)
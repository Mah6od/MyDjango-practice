from django.shortcuts import render
from django.views.generic import ListView
from .models import Profile, Link

# views
class LinkListView(ListView):
    # query for all the links Link.objects.all()
    # context = {'links':links}
    # return render(request, 'link_list.html', context)

    model = Link
    # template called model_list.html -> link_list.html
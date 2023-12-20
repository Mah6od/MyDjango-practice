from django.shortcuts import get_object_or_404, render
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Profile, Link
from django.urls import reverse_lazy

# views
class LinkListView(ListView):
    # query for all the links Link.objects.all()
    # context = {'links':links}
    # return render(request, 'link_list.html', context)

    model = Link
    # template called model_list.html -> link_list.html

class LinkCreateView(CreateView):
    # create froms.py file & form
    # check if this was a post or get request
    # return an empty form or save the form date

    model = Link
    fields = '__all__'
    success_url = reverse_lazy('link-list')
    # template model_form -> link_form.html

class LinkUpdateView(UpdateView):
    # create a form
    # check if a get request or a put request
    # either render the form or update and save in our db

    model = Link
    fields = ['text', 'url']
    success_url = reverse_lazy('link-list')
    # template model_form -> link_form.html

class LinkDeleteView(DeleteView):
    # take in a id/pk of an object
    # query to db for that object
    # check if it exists -> delete the object
    # return some template or forward to user to some url
    
    # send a form with a single 'confirm delete btn'
    # template - model_confirm_delete.html
    model = Link
    success_url = reverse_lazy('link-list')

## external profile view - could be a ListView or a function view
def profile_view(request, profile_slug):
    profile = get_object_or_404(Profile, slug=profile_slug)
    links = profile.links.all()
    context = {
        "profile": profile,
        "links": links
    }
    return render(request, 'link_plant/profile.html', context)
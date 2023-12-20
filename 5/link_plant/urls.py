from django.urls import path 
from .views import LinkListView

urlpatterns = [
    path('', LinkListView.as_view(), name="link-list"),
]

from django.urls import path 
from .views import LinkListView

# urls
urlpatterns = [
    path('', LinkListView.as_view(), name="link-list"),
]

from django.urls import path
from .views import homeview, trips_list

urlpatterns = [
    path('', homeview.as_view(), name='home'),
    path('dashboard/', trips_list, name="trip-list"),
]
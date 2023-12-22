from django.urls import path
from .views import homeview

urlpatterns = [
    path('', homeview.as_view(), name='home'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'), 
    path('buyers_number', views.buyers_number, name = 'buyers_number'),
    path('new_sell', views.new_sell, name = 'new_sell'),
]
''''''
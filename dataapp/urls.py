from django.urls import path
from . import views

urlpatterns = [
    path('insert_data/', views.insert_data_view, name='insert_data'),
]

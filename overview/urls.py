from django.urls import path
from  . import views

app_name='overview'

urlpatterns = [
    path('dashboard',views.index,name='dashboard'),
]
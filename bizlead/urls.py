from django.urls import path
from  . import views

app_name='bizlead'

urlpatterns = [
    path('businesslead',views.businesslead, name='businesslead'),
    path('addbusinesslead', views.addbusinesslead, name='addbusinesslead'),

    path('facilitydetails/<int:id>/',views.facilitydetails,name='facilitydetails'),
    path('adddemo',views.adddemo,name='adddemo'),

    path('tracker',views.tracker,name='tracker'),
    path('details/update/<int:pk>/',views.details_update,name='details_update'),
]
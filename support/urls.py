from django.urls import path
from  . import views


app_name='support'

urlpatterns = [
    path('supportcall',views.supportcall,name='supportcall'),
    path('addsupportcall',views.addsupportcall,name='addsupportcall'),
    path('addsupportcall/delete/<int:pk>/',views.addsupportcall_delete,name='addsupportcall_delete'),
    path('addsupportcall/update/<int:pk>/',views.addsupportcall_update,name='addsupportcall_update'),
    path('searchbar',views.searchbar,name='searchbar'),

    path('courtesycall',views.courtesycall,name='courtesycall'),
    path('addcourtesycall',views.addcourtesycall,name='addcourtesycall'),
    path('addcourtesycall/delete/<int:pk>/',views.addcourtesycall_delete,name='addcourtesycall_delete'),
    path('addcourtesycall/update/<int:pk>/',views.addcourtesycall_update,name='addcourtesycall_update'),

    path('bimonthlycall',views.bimonthlycall,name='bimonthlycall'),
    path('addbimonthlycall',views.addbimonthlycall,name='addbimonthlycall'),
    path('bimonthlycall/delete/<int:pk>/',views.bimonthlycall_delete, name='bimonthlycall_delete'),
    path('bimonthlycall/update/<int:pk>/',views.bimonthlycall_update, name='bimonthlycall_update'),

    
]
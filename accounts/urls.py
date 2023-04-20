from django.urls import path
from  . import views


app_name='accounts'

urlpatterns = [
    path('bills',views.bills,name='bills'),
    path('addnewbill',views.addnewbill,name='addnewbill'),

    path('receipts',views.receipts,name='receipts'),
    path('addreceipt', views.addreceipt, name='addreceipt'),
    path('addreceipt/delete/<int:id>/',views.addreceipt_delete,name='addreceipt_delete'),
    path('addreceipt/update/<int:id>/',views.addreceipt_update,name='addreceipt_update'),


    path('accdetails',views.accdetails,name='accdetails'),
    path('addclientacc', views.addclientacc, name='addclientacc'),
    path('addclientacc/delete/<int:id>/',views.addclientacc_delete,name='addclientacc_delete'),
    path('addclientacc/update/<int:id>/',views.addclientacc_update,name='addclientacc_update'),
    path('implementation/<int:id>/',views.implementation,name='implementation'),

    path('reports',views.reports, name='reports')
]

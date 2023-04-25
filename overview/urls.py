from django.urls import path
from  . import views

app_name='overview'

urlpatterns = [
    path('dashboard',views.index,name='dashboard'),
    path("", views.login_request, name="login"),
    path("register", views.register_request, name="register"),
    path("logout", views.logout_request, name= "logout"),
]
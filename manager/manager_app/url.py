from django.urls import path
from manager_app import views

urlpatterns=[
    path('',views.home,name='Home'),
    path('register/',views.sign_user,name='register'),
    path('login/',views.login_user,name='login'),
]
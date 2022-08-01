from tempfile import template
from django.urls import path 
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeDoneView,PasswordChangeView
from . import views


urlpatterns = [  
    path('',views.login_process,name='log'),
    path('login',views.login_process,name='log'), 
    path('register',views.register,name='reg'), 
    path('successpage',views.successpage,name='success'),
    path('home',views.home,name='home'), 
    path('logout',views.logout_process,name='logoutp'), 
    path('changepassword',PasswordChangeView.as_view(template_name='changepassword.html',success_url=reverse_lazy('passwordchangedone')),name="changepassword"), 
    path('passwordchangedone',PasswordChangeDoneView.as_view(template_name='passwordchangedone.html'),name='passwordchangedone')
]
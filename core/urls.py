from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm

app_name='core'
urlpatterns=[
      path('',views.index,name='index'),
      path('contact/',views.contact,name='contact'),
      path('signup/',views.signup,name='signup'),
      path('login/',auth_views.LoginView.as_view(authentication_form=LoginForm,template_name='./login.html'),name='login'),
      path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
]
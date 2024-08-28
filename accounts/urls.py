from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('login', views.Login_View, name='login'),
    path('signup', views.Signup_View, name='register'),
    path('logout', views.Logout_View, name='logout'),
]

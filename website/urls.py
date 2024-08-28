from django.urls import path
from website.views import *

app_name = 'website'

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('services/', services, name='services'),
    path('starter/', starter_page, name='starter_page'),
    path('resume/', resume_page, name='resume_page'),
]
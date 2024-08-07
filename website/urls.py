from django.urls import path
from website.views import index,about,call

urlpatterns = [
    path('',index),
    path('about/',about),
    path('call/',call),
]

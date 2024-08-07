from django.shortcuts import render

from django.http import HttpResponse,JsonResponse
def index(request):
    return render(request,'website/index.html')

def about(request):
    return render(request,'website/about.html')

def call(request):
    return render(request,'website/call.html')

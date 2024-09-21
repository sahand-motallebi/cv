from django.shortcuts import render, redirect
from website.forms import ContactForm
from django.contrib import messages


def index(request):
    return render(request, 'website/index.html')


def about(request):
    return render(request, 'website/about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'your ticket submited successfully')
            return redirect('website:services')
        else:
            messages.add_message(request, messages.ERROR, 'your ticket didnt submited')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'website/contact.html', context)


def resume(request):
    return render(request, 'website/resume.html')


def services(request):
    return render(request, 'website/services.html')


def starter_page(request):
    return render(request, 'website/starter-page.html')


def resume_page(request):
    return render(request, 'website/resume.html')

from django.shortcuts import render, redirect
from website.forms import ContactForm
from django.http import JsonResponse


def index(request):
    return render(request, 'website/index.html')


def about(request):
    return render(request, 'website/about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'Your ticket has been submitted successfully.'})
        else:
            # ارسال خطاها از جمله کپچا به صورت JSON
            return JsonResponse({'success': False, 'errors': form.errors.as_json()}, status=400)
    else:
        form = ContactForm()
    return render(request, 'website/contact.html', {'form': form})


def resume(request):
    return render(request, 'website/resume.html')


def services(request):
    return render(request, 'website/services.html')


def starter_page(request):
    return render(request, 'website/starter-page.html')


def resume_page(request):
    return render(request, 'website/resume.html')

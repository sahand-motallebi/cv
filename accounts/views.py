from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages


def Login_View(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                name = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=name, password=password)
                if user is not None:
                    login(request, user)
                    return JsonResponse({'status': 'success'})  # موفقیت
                else:
                    return JsonResponse({'status': 'error', 'message': 'Invalid username or password.'})  # نام کاربری یا رمز عبور نادرست
            else:
                return JsonResponse({'status': 'error', 'message': 'Invalid form submission.'})  # ارسال فرم نادرست

        form = AuthenticationForm()
        context = {'form': form}
        return render(request, 'accounts/login.html', context)
    else:
        return redirect('/')


@login_required
def Logout_View(request):
    logout(request)
    return redirect('/')


def Signup_View(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return JsonResponse({'success': True, 'message': 'User created successfully.'})
            else:
                return JsonResponse({'success': False, 'errors': form.errors}, status=400)
        form = UserCreationForm()
        context = {'form': form}
        return render(request, 'accounts/signup.html', context)
    return redirect('/')
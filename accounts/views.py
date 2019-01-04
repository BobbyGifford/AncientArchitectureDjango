from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404

from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .models import Profile


def register(request):
    if request.method == 'POST':
        # Fetch user values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        #     Password Check
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username taken")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email taken")
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=password, email=email,
                                                    first_name=first_name, last_name=last_name)
                    user_profile = Profile(user=user)

                    user.save()
                    user_profile.save()

                    messages.success(request, "Registered")
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def profile(request):
    context = {
        'profile': Profile(user=request.user)
    }
    return render(request, 'accounts/profile.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "Logged in")
            return redirect('index')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, "Logged out")
    return redirect('index')

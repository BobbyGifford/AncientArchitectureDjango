from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .models import Profile
from theories.models import Theory
from locations.models import Location


def register(request):
    if request.method == 'POST':
        # Fetch user values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']

        password = request.POST['password']
        password2 = request.POST['password2']

        #     Password Check
        if password == password2:
            if User.objects.filter(username=email).exists():
                messages.error(request, "Username taken")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email taken")
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=email, password=password, email=email,
                                                    first_name=first_name, last_name=last_name)
                    user_profile = Profile(user=user)

                    user.save()
                    user_profile.save()

                    messages.success(request, "Registered")
                    return redirect('login_user')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def profile(request):
    user_profile = Profile.objects.get(user=request.user)

    # Search for user's locations
    user_locations = Location.objects.filter(profile=user_profile).order_by('-upload_date')

    # Search for user's theories
    user_theories = Theory.objects.filter(profile=user_profile).order_by('-upload_date')

    context = {
        'profile': user_profile,
        'locations': user_locations,
        'theories': user_theories
    }

    return render(request, 'accounts/profile.html', context)


def edit_profile(request):
    user_profile = Profile.objects.get(user=request.user)
    context = {
        'profile': user_profile
    }

    if user_profile.user != request.user:
        return render(request, 'pages/index.html')

    if request.method == 'POST':
        new_description = request.POST['description']
        old_profile = Profile.objects.get(user=request.user)
        old_profile.description = new_description

        if 'profile_pic' in request.FILES:
            old_profile.profile_pic = request.FILES['profile_pic']

        old_profile.save()

        return render(request, 'pages/index.html')

    return render(request, 'accounts/edit_profile.html', context)


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
            return redirect('login_user')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return redirect('index')

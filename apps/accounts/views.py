from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from .forms import SimpleRegisterForm , ProfileUpdateForm


def register_view(request):
    # agar user login bo‘lgan bo‘lsa
    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == 'POST':
        form = SimpleRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            role = form.cleaned_data['role']

            # user yaratish
            user = User(username=username)
            user.set_password(password)  # xavfsiz hash
            user.save()

            # profile signal orqali bor — role beramiz
            profile = user.profile
            profile.role = role
            profile.save()

            # avtomatik login
            login(request, user)
            return redirect('profile')
    else:
        form = SimpleRegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    # login bo‘lgan user login sahifaga kirmaydi
    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def profile_view(request):
    profile = request.user.profile
    return render(request, 'accounts/profile.html', {'profile': profile})

@login_required
def profile_edit_view(request):
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=profile)

    return render(request, 'accounts/profile_edit.html', {'form': form})

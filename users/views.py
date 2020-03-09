from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, RegisterForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        i_form = RegisterForm(request.POST)
        if form.is_valid() and i_form.is_valid():
            form.save()
            i_form.save()
            messages.success(request, f'Account has been created! you can now login')
            return redirect('login')

    else:
        form = UserRegisterForm()
        i_form = RegisterForm()
    return render(request, 'users/register.html', {'form': form},{'i_form':i_form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'your account has been successfully updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context ={
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)
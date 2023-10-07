from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from user_profile.forms import UserUpdateForm, ProfileUpdateForm
from user_profile.models import Profile


@login_required
def my_profile(request):
    if request.method == 'GET':
        return render(request, 'user_profile/profile.html', {'title_site': 'Profile'})
    elif request.method == 'POST':
        return redirect('profile-update')


@login_required
def update_profile(request):
    if request.method == 'GET':
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        return render(request, 'user_profile/update.html',
                      {'user_form': user_form, 'profile_form': profile_form, 'title_site': 'Profile'})
    elif request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            print("YES")
            return redirect('profile')
        return render(request, 'user_profile/update.html',
                      {'user_form': user_form, 'profile_form': profile_form, 'title_site': 'Profile'})

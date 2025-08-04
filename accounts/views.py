
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
from .models import UserProfile

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            profile = UserProfile.objects.get(user=user)
            profile.department = form.cleaned_data['department']
            profile.save()

            messages.success(request, '🎉 Registration successful! You can now log in.')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        # validate
        if form.is_valid():
            # save user
            form.save()
            username= form.cleaned_data.get('username')
            print(form.cleaned_data)
            messages.success(request, 'Account createdd! You can no login')
            # redirect the user to the home page if the form is valid
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
    

@login_required
def profile(request):
    return render(request, 'users/profile.html')
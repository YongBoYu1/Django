from django.shortcuts import render, redirect
from django.contrib import messages
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
            messages.success(request, f'Account creates for {username} !')
            # redirect the user to the home page if the form is valid
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
    # if request.method == 'POST':
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         username = form.cleaned_data.get('username')
    #         messages.success(request, f'Account created for {username}!')
    #         return redirect('blog-home')
    # else:
    #     form = UserRegisterForm()
    # return render(request, 'users/register.html', {'form': form})
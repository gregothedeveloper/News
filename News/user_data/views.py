from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('auth:login')
    else:
        form = UserCreationForm()
    return render(request, 'user_data/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('list')
    else:
        form = AuthenticationForm()
    return render(request, 'user_data/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('auth:login')
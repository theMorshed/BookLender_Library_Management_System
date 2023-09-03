from django.shortcuts import render, redirect
from account.forms import RegistrationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user is None:
            return render(request, 'login.html', {'error': 'Username and password does not match'})
        login(request, user)
        return redirect('home')
    
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
        
    context = {'form': form}
    return render(request, 'register.html', context)

def user_logout(request):
    logout(request)
    return redirect('login')
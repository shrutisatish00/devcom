from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            #log the use in
            login(request, user)
            return redirect('/Blog/')
    else:    
        form = UserCreationForm() 
    return render(request,'newacc/signup.html', {'form':form})

def login_view(request):
    if request.method == 'POST':
        form= AuthenticationForm(data=request.POST)
        if form.is_valid():
            
            user = form.get_user()
            login(request,user)
            return redirect('/Blog/')
    else:
        form= AuthenticationForm()
    return render(request, 'newacc/login.html', {'form':form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('')
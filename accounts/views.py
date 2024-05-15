from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login

# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            #Log in user later
            user =form.save()
            login(request,user)
            print("Sign up successful")
            return redirect('accounts:login')
        else:
            print("Failed Sign up")
            return render(request, 'accounts/sign_up.html',{'form': form}) 
    else:
        form = UserCreationForm()
        print("Incorrect info")
    return render(request, 'accounts/sign_up.html',{'form': form})

def log_in(request):
    if request.method == "POST":
        form = AuthenticationForm(data= request.POST)

        if form.is_valid():
            print("Successful Login")
            #Login user
            user = form.get_user()
            login(request,user)
            return redirect('app1:list')
        else:
            print("Failed Login")
            return render(request, 'accounts/log_in.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'accounts/log_in.html', {'form': form})    

    
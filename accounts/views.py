from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            #Log in user later
            print("Sign up successful")
            return redirect('app1:list')
        else:
            print("Failed Sign up")
            return render(request, 'accounts/sign_up.html',{'form': form}) 
    else:
        form = UserCreationForm()
        print("Incorrect info")
    return render(request, 'accounts/sign_up.html',{'form': form})

    
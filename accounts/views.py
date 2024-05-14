from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def sign_up(request):
    form = UserCreationForm()
    return render(request, 'accounts/sign_up.html',{'form': form})
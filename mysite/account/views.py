from django.shortcuts import render
from .forms import UserLoginForm
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def user_login(request):
    if request.method=='POST':
       form=UserLoginForm(request.POST)
       if form.is_valid() :
        cd=form.cleaned_data
        user=authenticate(request,username=cd['username'],password=cd['password'])
        print(user)
        if user:
            login(request,user)
            return HttpResponse('Authentication successfully')
        else:   
            return HttpResponse('Invalid Login')
    else:
        form=UserLoginForm()
        return render(request,'account/login.html',{'form':form})
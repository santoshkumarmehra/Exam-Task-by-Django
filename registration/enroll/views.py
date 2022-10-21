from django.shortcuts import render,HttpResponseRedirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm,EditUserProfileForm,EditAdminProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required

# Create your vis here.

#Sign_up for user
def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request,"Account Created successfully !!")
            fm.save()
    else:
        fm = SignUpForm()    
    return render(request,'enroll/signup.html',{'form':fm})

#Login view function for user
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                # email = fm.data # print(email.items())# for i in email: # print(i)# print(uname)  # print(upass)
                user_object = authenticate(request,username=uname,password=upass)
                if user_object is not None:
                    login(request,user_object)
                    messages.success(request,"Logged in successfully !!")
                    return HttpResponseRedirect('/profile/')
        else:
            fm = AuthenticationForm()
        return render(request,'enroll/userlogin.html',{'form':fm})
    else:
        return HttpResponseRedirect('/profile/')

# profile for user
# @login_required(login_url='/login')
# @user_login
def user_profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            if request.user.is_superuser == True:
                fm = EditAdminProfileForm(request.POST,instance=request.user)
            else:
                fm = EditUserProfileForm(request.POST,instance=request.user)
            if fm.is_valid():
                messages.success(request,'Profile updated !!!')
                fm.save()
        else:
            if request.user.is_superuser == True:
                fm = EditAdminProfileForm(instance=request.user)
            else:
                fm = EditUserProfileForm(instance=request.user)
        return render(request,'enroll/profile.html', {'name': request.user,'form':fm})
    else:
        return HttpResponseRedirect('/login/')

# Logout for user
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

# change password
def user_change_pass(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request,'Password changed successfuly')
                return HttpResponseRedirect('/profile/')
        else:
            fm = PasswordChangeForm(user=request.user)
        return render(request,'enroll/changepass.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')


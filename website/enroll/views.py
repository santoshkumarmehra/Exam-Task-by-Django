import random
import re
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import Question, Result,UserData
# def result_store(request):


def checkemail(s):
    pat = "[a-zA-Z-_\.\-]+@[a-zA-Z]+\.[a-z]{2,3}$"
    if re.match(pat,s):
        return s
    else:
        return None

   
def mainexam(request):
    if request.method == 'POST':
        all_data = Result.objects.all()
        total_marks = 0
        for data in all_data:
            if data.question.answer == request.POST.get(str(data.id)):
                total_marks += 1
                # data.result = 1
                # data.save()
        UserData.objects.create(user=request.user, result=total_marks)
    return render(request, 'enroll/totalanswer.html', {'totalmarks':total_marks})
    

def examtask(request):
    if request.method == "POST":
        # all_data = Question.objects.order_by('?')[:3]
        question = set(Question.objects.all())
        all_data = random.sample(question,3)
        if not Result.objects.all():
            for ques in all_data:
                Result.objects.create(student_name=request.user, question=ques, result='0')        
        question = Result.objects.filter(student_name=request.user)
        # print(question)
        return render(request, 'enroll/examtask.html', {'qs':question})
    question = Result.objects.filter(student_name=request.user)
    return render(request, 'enroll/examtask.html', {'qs':question})
     

# Sign_up for user
def sign_up(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        mailvalidation = checkemail(email)
        if first_name == '' or last_name == '' or email == '' or password == '' :
            return render(request, 'enroll/signup.html')
        elif  mailvalidation == None:
            return render(request, 'enroll/signup.html')
        else:
            User.objects.create(username=first_name,first_name=first_name, last_name=last_name, email=email, password=make_password(password))
    return render(request, 'enroll/signup.html')#,{'form':user_detail})


def user_login(request):
    # import pdb;pdb.set_trace()
    if request.method == "POST":
        email = request.POST.get('email')
        # print(email)
        password = request.POST.get('password')
        user_data= User.objects.all()
        for data in user_data:
            if data.email == email:
                user_object = authenticate(request, username=data.username, password=password)
                # print(user_object)
                if user_object is not None:
                    login(request, user_object)
                    return redirect('/profile/')
                
        return render(request, 'enroll/userlogin.html')
    else:
        # user_detail = AuthenticationForm()
        return render(request, 'enroll/userlogin.html')


# profile for user
def user_profile(request):
    # import pdb;pdb.set_trace()
    if request.user.is_authenticated:
        return render(request, 'enroll/profile.html')
    return redirect('/login/')


def user_logout(request):
    Result.objects.all().delete()
    # import pdb;pdb.set_trace()
    logout(request)
    return redirect('/login/')


def home(request):
    return render(request, 'enroll/home.html')
















# all_question = random.sample(question,3)
    # print(q)
    
    # for i in question:
        # return HttpResponseRedirect('/mainexam/')
    # return mainexam(request,q)e

 # print(all_question)
    # import pdb;pdb.set_trace()
    # question = set(Question.objects.all())
    # all_question = random.sample(question,3)
    # print(all_question)
    # all_question = q

# import pdb;pdb.set_trace()
    # if request.method == "POST":
    # q=Question.objects.order_by('?')[:3]
        
    # return render(request, 'enroll/examtask.html', {'qs':q})

# for data in all_data:
        #     if data.answer == request.POST.get(str(data.id)):
                # total_marks = total_marks + 1

            # return render(request, 'enroll/totalanswer.html', {'totalmarks':total_marks})
    #     return HttpResponseRedirect('/mainexam/')
    #     question = set(Question.objects.all())
    #     all_question = random.sample(question,3)
    #     # return HttpResponseRedirect('/mainexam/')
    #     mainexam(request,all_question)

   
        # print(request.POST)
    #     all_data = Question.objects.all()
    #     total_marks = 0
    #     for data in all_data:
    #         if data.answer == request.POST.get(str(data.id)):
    #             total_marks = total_marks + 1
    #     Result.objects.create(student_name=request.user, result=total_marks)        
    #     return render(request, 'enroll/totalanswer.html', {'totalmarks':total_marks})
    # question = set(Question.objects.all())
    # all_question = random.sample(question,3)
    # return redirect("/mainexam/")
    # return mainexam(request, all_question)









# print(i.id)
            # print(request.POST.get(str(i.id)))
            # print(i)
            # print(i)
            # print(i.question)
            # print(i.option_1)
            # print(i.option_2)
        #     print(i.answer,request.POST.get(str(i.id)))
        # question = list(Question_model.objects.values('id', 'question','option_1','option_2','option_3','option_4'))
        # print(question)




# def user_login(request):
#     if request.method == "POST":
#         # import pdb;pdb.set_trace()
#         email = request.POST.get('username')
#         password = request.POST.get('password')
#         try:
#             user_info=User.objects.filter(email=email).get()
#         except:
#             print("email not resgistered")
#             return render(request,'enroll/userlogin.html')
#         user_object = authenticate(request,username=user_info.username,password=password)
#         if user_object is not None:
#             return render(request,'enroll/profile.html')
#         else:
#             print("password incorrect")
#             return render(request,'enroll/userlogin.html')
#     else:
#         # user_detail = AuthenticationForm()
#         return render(request,'enroll/userlogin.html')





# from .forms import SignUpForm  
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.hashers import check_password
# from cryptography.fernet import Fernet



        # hash_object = hashlib.md5(password.encode())
        # md5_hash = hash_object.hexdigest()
        # print(md5_hash)
        # print(check_password('the default password', u.password))
        # print(email)
        # print(password)
        # user_detail = AuthenticationForm(request=request,data=request.POST)
        # import pdb;pdb.set_trace()
        # if user_detail.is_valid():
            # uemail = user_detail.cleaned_data['email']
            # upass = user_detail.cleaned_data['password']
            # print(email)
            # print(password)
        # import pdb;pdb.set_trace()
        # print(user_object)
            # messages.success(request,"Logged in successfully !!")
            # login(request,user_object)
    # elif request.method != "POST":
    #     return render(request,'enroll/userlogin.html')




        # key = Fernet.generate_key()
        # fernet = Fernet(key)
        # encrypt_password = fernet.encrypt(password.encode())
        # print(first_name)
        # print(type(first_name))
        # print(last_name)
        # print(type(last_name))
        # print(email)
        # print(password)
        # except:
        #     messages.success(request,'user name already exist')
            # return render(request,'enroll/signup.html')
    # else:
    # user_detail = SignUpForm()    
    # return render(request,'enroll/signup.html')z

# def sign_up(request):    
#     return render(request,'enroll/signup.html')


# #Login view function for user
# @login_required(login_url='/login/')
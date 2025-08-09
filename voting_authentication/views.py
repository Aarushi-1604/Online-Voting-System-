from django.shortcuts import render,redirect
from voting_authentication.models import CustomUser
from django.contrib.auth import authenticate,login
from django.core.mail import send_mail
from django.contrib import messages
import random

# Create your views here.

def register(request):
    if request.method=="POST":
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if CustomUser.objects.filter(username=uname).exists():
            messages.warning(request,'This Username already exists')
            return redirect('register')
        elif CustomUser.objects.filter(email=email).exists():
            messages.warning(request,"This Email already exists")
            return redirect('register')
        elif pass1==pass2 and ' ' in pass1:
            messages.warning(request,'The password cannot contain spaces')
            return redirect('register')
        elif pass1==pass2 and len(pass1)<8:
            messages.warning(request,'The password must be at least 8 characters long')
            return redirect('register')
        elif pass1==pass2 and len(pass1)>=8:
            otp=str(random.randint(100000,999999))
            request.session['otp']=otp
            request.session['username']=uname
            request.session['email']=email
            request.session['password1']=pass1
            send_mail(
                'Your OTP for Email Verification',
                f'Your OTP for email verification is {otp}',
                'dreamkatcher.insomnia@gmail.com',
                [email],
                fail_silently=False,
            )
            return redirect('email_verification')
        else:
            messages.warning(request,'Passwords do not match. Check again')
            return redirect('register')
    else:
        return render(request,'voting_register.html')

def log_in(request):
    if request.method=="POST":
        username=request.POST.get('username')
        passw=request.POST.get('pass')
        user=authenticate(request,username=username,password=passw)
        if user is not None:
            login(request,user)
            print(request.user.id,username)
            request.session['show_welcome_message']=True
            return redirect('home')
        else:
            messages.error(request,'Password does not belong to the username. Try Again')
            return redirect('login')
    return render(request,'voting_login.html')

def verification(request):
    if request.method=="POST":
        entered_otp=request.POST.get('otp')
        stored_otp=request.session.get('otp')
        if entered_otp==stored_otp:
            uname=request.session.get('username')
            email=request.session.get('email')
            pass1=request.session.get('password1')
            if request.session.get('reset_password'):
                new_password=pass1
                user=CustomUser.objects.get(username=uname,email=email)
                user.set_password(new_password)
                user.save()
                del request.session['otp']
                del request.session['username']
                del request.session['email']
                del request.session['password1']
                messages.success(request,'Your password has been reset successfully! You can now login using your new password')
                return redirect('login')
            else:
                my_user=CustomUser.objects.create_user(username=uname,email=email,password=pass1)
                my_user.save()
                del request.session['otp']
                del request.session['username']
                del request.session['email']
                del request.session['password1']
                messages.success(request,"Your account has been created successfully! You can now login using your credentials")
                return redirect('login')
        else:
            messages.error(request,'Your OTP did not match. Please try again')
            return redirect('email_verification')
    else:
        return render(request,'voting_verification.html')
    
def forgot_password(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        user=CustomUser.objects.filter(username=username,email=email).first()
        if user and pass1==pass2:
            otp=str(random.randint(100000,999999))
            request.session['otp']=otp
            request.session['username']=username
            request.session['email']=email
            request.session['password1']=pass1
            request.session['reset_password']=True
            send_mail(
                'Your OTP for Email Verification',
                f'Your OTP for email verification is: {otp}',
                'dreamkatcher.insomnia@gmail.com',
                [email],
                fail_silently=False,
            )
            return redirect('email_verification')
        elif user is None:
            messages.warning(request, 'Email and Username do not match')
            return redirect('forgot_password')
        elif pass1!=pass2:
            messages.warning(request,'Password and Confirm Password do not match')
            return redirect('forgot_password')
    else:
        return render(request,'voting_forgot_password.html')

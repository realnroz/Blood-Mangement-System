from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from . models import BloodDonor
from django.shortcuts import redirect, render
from django.contrib import messages
from . forms import DonorProfileForm, ProfileUpdateForm , ProfileUpdateForm, StatusUpdateForm
from accounts.forms import UserRegistrationForm, UserUpdateForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required

from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


def registration(request):
    if request.method == 'POST':
        userform = UserRegistrationForm(request.POST)
        profileform = DonorProfileForm(request.POST,request.FILES)
        if userform.is_valid() and profileform.is_valid():
            contact_number=str(profileform.cleaned_data.get('mobile_number'))
            if len(contact_number) != 10:
                messages.warning(request,'Mobile number should be exactly 10 digits long ')
            else:
                profileform.instance.first_name=profileform.instance.first_name.title()
                profileform.instance.last_name=profileform.instance.last_name.title()
                profileform.instance.city=profileform.instance.city.title()
                user = userform.save()

                profile = profileform.save(commit=False)
                profile.user = user
                profileform.save()

                user_name=profileform.cleaned_data.get('first_name')

                subject ='Welcome to bMS.'
                message = f'''
 Hello {user_name} . Welcome to BMS .Thank you for registering as a blood donor .

  

            Donate blood , save lives.    
                                                                    -TEAM BMS
                '''
            

                # send_mail(
                #     subject,
                #     message,
                #     settings.EMAIL_HOST_USER,
                #     [user.email],
                #     fail_silently = False, 
                # )

                
                messages.success(request,f'Account successfully created for {user_name.title()}')

                return redirect('home')
    else:
        userform = UserRegistrationForm()
        profileform = DonorProfileForm()
    context ={
        'title' : 'Registration',
        'userform': userform,
        'profileform' : profileform

    }
    
    return render(request, 'blood_donor/donor_registration.html',context)


def donorLogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request,email=email,password=password)
        if user is not None:
            login(request,user)
            """token, created = Token.objects.get_or_create(user=user)
            response = HttpResponseRedirect(reverse('profile'))
            response.set_cookie('token',str(token))"""
            messages.success(request,'You are successfully logged in.')
            return redirect('profile')
        else:
            messages.warning(request,'Invalid Credentials.')
            return redirect('home')

@login_required
def donorLogout(request):
    logout(request)
    messages.success(request,'You are successfully logged out.')
    return redirect('home')

@login_required
def donorProfile(request):

    context={
        
        'title' : 'Donor Profile'
    }
    return render(request,'blood_donor/donor_profile.html',context)

@login_required
def editInformation(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.blooddonor)
        if u_form.is_valid() and p_form.is_valid():
            contact_number=str(p_form.cleaned_data.get('mobile_number'))
            if len(contact_number) != 10:
                messages.warning(request,'Mobile number should be exactly 10 digits long ')
            else:
                p_form.instance.first_name=p_form.instance.first_name.title()
                p_form.instance.last_name=p_form.instance.last_name.title()
                p_form.instance.city=p_form.instance.city.title()
                u_form.save()
                p_form.save()

                messages.success(request,f'Your information has been successfully updated.')
                return redirect('profile')
    
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.blooddonor)
    context={
        'u_form' : u_form,
        'p_form' : p_form,
        'title' : 'Edit Information'
    }
    return render(request,'blood_donor/edit_information.html',context)

@login_required
def deleteAccount(request):
    request.user.delete()
    messages.success(request,f'Your account has been successfully deleted. You cannot login anymore.')
    return redirect('home')

@login_required
def setStatus(request):
    if request.method =='POST':
        s_form = StatusUpdateForm(request.POST,instance=request.user.blooddonor)
        if s_form.is_valid():
            s_form.save()
            messages.success(request,f'You have updated your status for blood donation.')
            return redirect('profile')
    else:
        s_form = StatusUpdateForm(instance=request.user.blooddonor)
    context={
        's_form' : s_form,
        'title' : 'Set Status'
    }
    return render(request,'blood_donor/set_status.html',context)
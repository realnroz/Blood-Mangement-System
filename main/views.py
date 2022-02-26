
from django.shortcuts import render,redirect
from django.contrib import messages
from blood_donor.models import BloodDonor
from django.views import View

from accounts.models import User
# Create your views here.

from django.core.mail import send_mail
from django.conf import settings

from blood_donor.views import donorLogin

def home(request):
    donors = BloodDonor.objects.all()
    context ={
        'donors' : donors
    }
    return render(request,'main/index.html',context)

def requestBlood(request):
    if request.method == 'POST':
        location = request.POST.get('Location')
        contact_info =str(request.POST.get('ContactInfo'))
        blood_group =request.POST.get('BloodGroup')
        if len(contact_info) != 10:
            messages.warning(request,'Contact number must be exactly 10 digits long')
        else:
            matched_donors = BloodDonor.objects.filter(blood_group=blood_group,city__icontains=location,is_available='Yes')
            matched_donors_count =matched_donors.count()
            context={
                    'matched_donors':matched_donors,
                    'title':'Search Results',
                    'matched_donors_count':matched_donors_count,
                    'location': location.title(),
                }
            
            subject =f' Blood Requested in {location.title()}.'
            message = f'''
    You have been matched as a donor for the blood group : '{blood_group}'. If you are willing to donate the blood.Connect with the seeker at:
    
                                            Contact Number = {contact_info}

                                               Donate Blood, Save lives.
                                                                                                                                    Regards,
                                                                                                                                    -TEAM BMS
                '''
            
            for donor in matched_donors:
                send_mail(
                    subject,
                    message,
                    settings.EMAIL_HOST_USER,
                    [donor.user],
                    fail_silently = False, 
                )

            return render(request,'main/searchresults.html',context)
       
    return render(request,'main/requestblood.html',{'title':'Request Blood'})


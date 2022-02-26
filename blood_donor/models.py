from django.db import models
from accounts.models import User
import uuid
# Create your models here.

class BloodDonor(models.Model):
    user =models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)

    gender_choices=[
        ('male','Male'),
        ('female','Female'),
    ]
    gender=models.CharField(
        max_length=6,
        choices=gender_choices,
    )

    dob=models.DateField(blank=True,null=True)

    city=models.CharField(max_length=50)


    blood_group_list=[
        ("A+" , "A+"),
        ("A-" , "A-"),
        ("B+" , "B+"),
        ("B-" , "B-"),
        ("O+" , "O+"),
        ("O-" , "O-"),
        ("AB+" , "AB+"),
        ("AB-" , "AB-"),
    ]
    blood_group=models.CharField(
        max_length=3,
        choices=blood_group_list,
    )

    mobile_number=models.CharField(max_length=10)

    is_available_choices=[
        ('Yes','Yes'),
        ('No','No')
    ]

    is_available=models.CharField(
        max_length=5,
        choices=is_available_choices,
        default="Yes"
    )

    profile_image = models.ImageField(null = True, blank=True, upload_to ='profiles/', default ='profiles/user-default.jpg')

    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.first_name+" "+self.last_name


  
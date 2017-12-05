from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from apps.base.models.create_update_model import CreateUpdateModel
GENDER_CHOICES=(('M', 'M'), ('F', 'F'),('O','O'))
from apps.base.constants import DEFAULT_NATIONALITY_INDIAN
from apps.base.models.address import Address

class Politician(CreateUpdateModel):
    user=models.OneToOneField(User)
    middle_name=models.CharField(max_length=250,null=True,blank=True)
    about_me=models.CharField(max_length=250,null=True,blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True, choices=GENDER_CHOICES)
    birth_place=models.CharField(max_length=250,null=True,blank=True)
    nationality=models.CharField(max_length=250,default=DEFAULT_NATIONALITY_INDIAN)
    mobile=models.BigIntegerField(null=True,blank=True)
    aadhaar_uid=models.CharField(max_length=250,null=True,blank=True)
    Voter_uid=models.CharField(max_length=250,null=True,blank=True)
    religion=models.CharField(max_length=250,null=True,blank=True)
    caste=models.CharField(max_length=250,null=True,blank=True)
    family_description=models.TextField(null=True,blank=True)
    profile_pic=models.ImageField(null=True,blank=True)
    favourite_political_party=models.CharField(max_length=250,null=True,blank=True)
    favourite_political_leader=models.CharField(max_length=250,null=True,blank=True)
    permanent_address=models.ForeignKey(Address,null=True,blank=True,related_name='politician_permanent_address')
    current_address=models.ForeignKey(Address,null=True,blank=True,related_name='politician_current_address')

    def get_education(self):
        return self

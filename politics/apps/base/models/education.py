from django.db import models
from django.contrib import admin
from apps.base.models.create_update_model import CreateUpdateModel
from apps.base.constants import EDUCATION_CATEGORY_CHOICES,EDUCATION_GRADE_CHOICES
from apps.base.models.politician import Politician


class PoliticianEducation(CreateUpdateModel):
    category=models.CharField(max_length=250,choices=EDUCATION_CATEGORY_CHOICES)
    name=models.CharField(max_length=250,null=True,blank=True)
    specialization=models.CharField(max_length=250,null=True,blank=True)
    university=models.CharField(max_length=250,null=True,blank=True)
    grade=models.CharField(max_length=250,choices=EDUCATION_GRADE_CHOICES)
    start=models.DateField(null=True,blank=True)
    end=models.DateField(null=True,blank=True)
    politician=models.ForeignKey(Politician,null=True,blank=True)

    def __str__(self):
        return self.category

admin.site.register(PoliticianEducation)
from apps.base.models.create_update_model import CreateUpdateModel
from django.db import models
from apps.base.constants import RELATION_TYPE_CHOICES
from apps.base.models.politician import Politician

class PoliticianFamily(CreateUpdateModel):
    relation=models.CharField(max_length=250,choices=RELATION_TYPE_CHOICES)
    name=models.CharField(max_length=250)
    date_of_birth=models.DateField(null=True,blank=True)
    occupation=models.CharField(max_length=250,null=True,blank=True)
    politician=models.ForeignKey(Politician,null=True,blank=True)

    class Meta:
        verbose_name="Family"
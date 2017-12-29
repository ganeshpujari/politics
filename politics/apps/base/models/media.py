from django.db import models
from apps.base.models.create_update_model import CreateUpdateModel
from apps.base.constants import MEDIA_TYPE_CHOICES
from apps.base.models.politician import Politician

class Media(CreateUpdateModel):
    title=models.CharField(max_length=250)
    url=models.CharField(max_length=250,null=True,blank=True)
    description=models.TextField(null=True,blank=True)

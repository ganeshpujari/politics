from apps.base.models.create_update_model import CreateUpdateModel
from apps.base.constants import ASSETS_TYPE_CHOICES
from apps.base.models.politician import Politician
from django.db import models


class PoliticianAssets(CreateUpdateModel):
    type=models.CharField(max_length=250,choices=ASSETS_TYPE_CHOICES)
    current_price=models.BigIntegerField(default=0)
    politician=models.ForeignKey(Politician,null=True,blank=True)
    name=models.CharField(max_length=250)
from apps.base.models.address import Location
from django.db import models
from apps.base.models.politician import Politician
from apps.base.constants import POLITICIAL_WORK_TYPE_CHOICES,WORK_TYPE_POLITICAL
from apps.base.models.media import Media


class Work(Location):
    type=models.CharField(max_length=250,choices=POLITICIAL_WORK_TYPE_CHOICES,default=WORK_TYPE_POLITICAL)
    title=models.CharField(max_length=250)
    description=models.TextField(null=True,blank=True)
    start = models.DateField(null=True, blank=True)
    end = models.DateField(null=True, blank=True)
    politician = models.ForeignKey(Politician, null=True, blank=True)
    media=models.ManyToManyField(Media,null=True,blank=True)


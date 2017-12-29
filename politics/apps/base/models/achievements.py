from apps.base.models.address import Location
from django.db import models
from apps.base.models.politician import Politician

class Achievements(Location):
    title=models.CharField(max_length=250)
    start = models.DateField(null=True, blank=True)
    end = models.DateField(null=True, blank=True)
    politician = models.ForeignKey(Politician, null=True, blank=True)

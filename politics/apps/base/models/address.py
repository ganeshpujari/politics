from django.db import models
from django.utils.translation import ugettext_lazy as _
import pytz
import googlemaps
from crum import get_current_request
TIME_ZONE = "America/Los_Angeles"
from apps.base.constants import ADDRESS_TYPE_CHOICE
from django.contrib import messages
from django.contrib import admin
from apps.base.models.create_update_model import CreateUpdateModel

def getLatLng(address):
    try:
        gmaps = googlemaps.Client(key='AIzaSyBNMx4wdjY6Xz5EhvOUA8h_VHTWvjzeDf0')
        geocode_result = gmaps.geocode(address)
        a=geocode_result[0]['geometry']['location']
        lat=a['lat']
        lng=a['lng']
        return (lat,lng)
    except:
        req = get_current_request()
        storage = messages.get_messages(req)
        storage.used = True
        messages.error(req, 'Invaid Address Please correct it')
        return (0,0)

class Location(CreateUpdateModel):
    city=models.CharField(max_length=250,null=True,blank=True)
    state=models.CharField(max_length=250,null=True,blank=True)
    country=models.CharField(max_length=250,null=True,blank=True)
    latitude = models.FloatField(
        null=True,
        blank=True,
        verbose_name=_("latitude")
    )

    longitude = models.FloatField(
        null=True,
        blank=True,
        verbose_name=_("longitude")
    )
    class Meta:
        abstract=True


class Address(Location):
    address1=models.CharField(max_length=250,null=True,blank=True)
    address2=models.CharField(max_length=250,null=True,blank=True)
    address3=models.CharField(max_length=250,null=True,blank=True)
    postal_code=models.BigIntegerField(null=True,blank=True)
    address_type=models.CharField(max_length=250,null=True,blank=True,choices=ADDRESS_TYPE_CHOICE)

    timezone = models.CharField(
        max_length=250,
        default=TIME_ZONE,
        choices=[(x, x) for x in pytz.all_timezones],
        verbose_name=_("timezone")
    )
    class Meta:
        pass
        # abstract = True



    # def save(self, *args, **kwargs):
    #     pass
        # if not self.latitude:
        # addForLatLng = str(self.address1) + "," + str(self.address2) + "," + str(self.address3) + "," + str(self.city)+ "," + str(self.state)+ "," + str(self.country)
        # latitude, longitude = getLatLng(addForLatLng)
        # self.latitude=latitude
        # self.longitude=longitude

admin.site.register(Address)
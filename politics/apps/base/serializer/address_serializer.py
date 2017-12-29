from rest_framework import serializers
from apps.base.models.address import Address


class AddressSerializerComplete(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields =('id','address1','address2','address3','city','postal_code','state','country','address_type','latitude','longitude','timezone')




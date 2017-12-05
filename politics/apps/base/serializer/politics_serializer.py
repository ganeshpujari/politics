from rest_framework import serializers
from apps.base.models.politician import Politician
from apps.base.serializer.user_serializer import UserSerializer
from apps.base.models.education import PoliticianEducation
from apps.base.serializer.education_serializer import PoliticianEducationSerializer
from apps.base.serializer.address_serializer import AddressSerializerComplete
from apps.base.serializer.user_serializer import UserSerializerMin

class PoliticianSerializer(serializers.ModelSerializer):
    user=UserSerializer()
    education = serializers.SerializerMethodField('get_my_education')
    permanent_address=AddressSerializerComplete()
    current_address=AddressSerializerComplete()


    def get_my_education(self,obj):
        poliObj= PoliticianEducation.objects.filter(politician=obj)
        serializer=PoliticianEducationSerializer(poliObj,many=True)
        return serializer.data

    class Meta:
        model = Politician
        fields =('id','user','date_of_birth','gender','birth_place','nationality','education','permanent_address','current_address')

class PoliticianSerializerMicro(serializers.ModelSerializer):
    class Meta:
        model = Politician
        fields =('id','user','date_of_birth','gender','birth_place','nationality')


class PoliticianSerializerMin(serializers.ModelSerializer):
    user=UserSerializerMin()
    class Meta:
        model = Politician
        fields =('id','user','date_of_birth','gender','birth_place','nationality')

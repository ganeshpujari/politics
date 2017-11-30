from rest_framework import serializers
from apps.base.models.politician import Politician
from apps.base.serializer.user_serializer import UserSerializer
from apps.base.models.education import PoliticianEducation
from apps.base.serializer.education_serializer import PoliticianEducationSerializer


class PoliticianSerializer(serializers.ModelSerializer):
    user=UserSerializer()
    education = serializers.SerializerMethodField('get_my_education')

    def get_my_education(self,obj):
        poliObj= PoliticianEducation.objects.filter(politician=obj)
        serializer=PoliticianEducationSerializer(poliObj,many=True)
        return serializer.data

    class Meta:
        model = Politician
        fields =('id','user','date_of_birth','gender','birth_place','nationality','education')



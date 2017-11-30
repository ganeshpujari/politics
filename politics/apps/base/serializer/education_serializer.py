from rest_framework import serializers
from apps.base.models.education import PoliticianEducation

class PoliticianEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoliticianEducation
        fields =('id','category','name','specialization','university','grade','start','end')


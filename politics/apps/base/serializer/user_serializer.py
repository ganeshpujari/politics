from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    group = serializers.SerializerMethodField('getFirstGroup')

    def getFirstGroup(self, obj):
        groups = obj.groups.all()
        grp = ''
        if len(groups) > 0:
            grp = groups[0].name
        return grp

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'group', 'first_name', 'last_name')
        depth = 1
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "politics.settings")
import django
django.setup()
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token as TK

userObj=User.objects.get(username=9028230101)
l=userObj.groups.values_list('name',flat=True)
print(l)

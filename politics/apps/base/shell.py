import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "politics.settings")
import django
django.setup()
from django.contrib.auth.models import User
from apps.base.models.politician import Politician
from apps.base.models.voter import Voter
from datetime import datetime
from apps.base.models.education import PoliticianEducation
dt=datetime.now()
import random

EDUCATION_CATOGORY_LIST=['ssc','hsc','diploma','graduation','post_graduation','other']
GRADE_LIST=['fail','pass','first_class','second_class','higher_second_class','pursuing']

# for i in range(10000,100000):
#     try:
#         usrObj=User()
#         usrObj.username="user"+str(i)
#         usrObj.first_name="fff"+str(i)
#         usrObj.last_name="lll"+str(i)
#         usrObj.email="eee"+str(i)+"rikoouu.com"
#         usrObj.save()
#
#         poliObj=Politician()
#         poliObj.user =usrObj
#         poliObj.date_of_birth =dt
#         poliObj.gender ='M'
#         poliObj.birth_place ='shriramput'
#         poliObj.save()
#     except(Exception,)as e:
#         print(e)


def set_education():
    try:
        poliObjs=Politician.objects.all()
        for pObj in poliObjs:
            for i in range(4):
                eduObj=PoliticianEducation()
                eduObj.category = random.choice(EDUCATION_CATOGORY_LIST)
                eduObj.name = 'ssc'
                eduObj.specialization = 'school'+str(pObj.user.username)
                eduObj.university = 'kop'+str(pObj.user.username)
                eduObj.grade =random.choice(GRADE_LIST)
                eduObj.start =dt
                eduObj.end =dt
                eduObj.politician=pObj
                eduObj.save()
    except (Exception,)as e:
        print(e)

set_education()
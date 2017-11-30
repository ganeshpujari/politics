
from django.conf.urls import url
from apps.base.api.politician import PoliticianList

urlpatterns = [
    url(r'^politicians/', PoliticianList.as_view({'get':'get',})),

]


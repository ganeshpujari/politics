from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotAcceptable
from apps.base.util.filter_params_util import get_filter_params
from apps.base.models.politician import Politician
from apps.base.serializer.politics_serializer import PoliticianSerializer

class PoliticianList(viewsets.ModelViewSet):
    # authentication_classes = (SessionAuthentication,TokenAuthentication)
    # permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return

    def get(self, request,format='json'):
        filterParams = get_filter_params(request.query_params, {})
        poliObjs=Politician.objects.filter(**filterParams)
        serializer=PoliticianSerializer(poliObjs,many=True)
        return Response(serializer.data)


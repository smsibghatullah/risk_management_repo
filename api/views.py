from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item, AuditProgramRepo, RiskRepo
from .serializers import ItemSerializer, AuditProgramRepoSerializer, RiskRepoSerializer

@api_view(['GET'])
def getData(request):
    items =  Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getRiskData(request):
    items =  RiskRepo.objects.all()
    serializer = RiskRepoSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getAuditProgramData(request):
    items =  AuditProgramRepo.objects.all()
    serializer = AuditProgramRepoSerializer(items, many=True)
    return Response(serializer.data)
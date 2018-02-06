from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import RiskTypeListSerializer, RiskTypeDetailSerializer

from risk_management.risk_type.models import RiskType


class RiskTypeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = RiskType.objects.all()
    serializer_class = RiskTypeListSerializer

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = RiskTypeDetailSerializer
        return super(RiskTypeViewSet, self).retrieve(request,*args,**kwargs)



class WebAppIndex(APIView):

    def get(self,request):
        return render(request, 'index.html')

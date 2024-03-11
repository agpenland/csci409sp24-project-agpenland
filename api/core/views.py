from django.shortcuts import render
from rest_framework import viewsets
from .models import Vessel
from .models import VesselSchedule
from .models import BillOfLading
from .models import Container
from .serializers import VesselSerializer
from .serializers import VesselScheduleSerializer
from .serializers import BillOfLadingSerializer
from .serializers import ContainerSerializer

# Create your views here.

class VesselViewSet(viewsets.ModelViewSet):
    queryset = Vessel.objects.all()
    serializer_class = VesselSerializer

class VesselScheduleViewSet(viewsets.ModelViewSet):
    queryset = VesselSchedule.objects.all()
    serializer_class = VesselScheduleSerializer

class BillOfLadingViewSet(viewsets.ModelViewSet):
    queryset = BillOfLading.objects.all()
    serializer_class = BillOfLadingSerializer

class ContainerViewSet(viewsets.ModelViewSet):
    queryset = Container.objects.all()
    serializer_class = ContainerSerializer

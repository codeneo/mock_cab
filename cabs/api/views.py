from cabs.models import Cab
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView
    )
from .serializers import (
    ListCabSerializer,
    CreateCabSerializer,
    RetrieveCabSerializer,
    UpdateCabSerializer
    )
from .permissions import IsDriver, IsOwner

class ListCabView(ListAPIView):
    queryset = Cab.objects.all()
    serializer_class = ListCabSerializer

class CreateCabView(CreateAPIView):
    queryset = Cab.objects.all()
    serializer_class = CreateCabSerializer
    # permission_classes = [IsDriver]

class RetrieveCabView(RetrieveAPIView):
    queryset = Cab.objects.all()
    serializer_class = RetrieveCabSerializer

class UpdateCabView(UpdateAPIView):
    queryset = Cab.objects.all()
    serializer_class = UpdateCabSerializer
    # permission_classes = [IsOwner]
from trips.models import Trip
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView
    )
from .serializers import (
    ListTripSerializer,
    CreateTripSerializer,
    RetrieveTripSerializer,
    UpdateStartTripSerializer,
    UpdateEndTripSerializer
    )
from .permissions import IsDriver, IsRider, IsOwner

class ListTripView(ListAPIView):
    serializer_class = ListTripSerializer

    def get_queryset(self):
        user = self.request.user
        if user.account_type == 'rider':
            return Trip.objects.filter(passenger=user.id)
        if user.account_type == 'driver':
            vehicle = Cab.objects.get(owner=user.id)
            return Trip.objects.filter(vehicle=vehicle.id)

class CreateTripView(CreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = CreateTripSerializer
    # permission_classes = [IsRider]

class RetrieveTripView(RetrieveAPIView):
    queryset = Trip.objects.all()
    serializer_class = RetrieveTripSerializer

class UpdateStartTripView(UpdateAPIView):
    queryset = Trip.objects.all()
    serializer_class = UpdateStartTripSerializer
    # permission_classes = [IsOwner]

class UpdateEndTripView(UpdateAPIView):
    queryset = Trip.objects.all()
    serializer_class = UpdateEndTripSerializer
    # permission_classes = [IsOwner]

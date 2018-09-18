from rest_framework import serializers
from trips.models import Trip
from cabs.models import Cab
from rest_framework.exceptions import PermissionDenied

class ListTripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ('id', 'latitude_start', 'longitude_start', 'latitude_end', 'longitude_end', 'vehicle', 'passenger')

class CreateTripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ('id', 'latitude_start', 'longitude_start', 'latitude_end', 'longitude_end', 'vehicle', 'passenger')

    def create(self, validated_data):
        passenger = validated_data['passenger']
        if passenger.account_type == 'driver':
            raise PermissionDenied('The passenger cannot be a Driver.')
        # Lock vehicle instance
        vehicle = Cab.objects.select_for_update.get(validated_data['vehicle'].id)
        if vehicle.status != 'online':
            raise PermissionDenied('The Cab isn\'t available for hire')
        # Change vehicle status
        vehicle.status = 'waiting'
        vehicle.save()
        # Create Trip with the vehicle
        return Trip.objects.create(**validated_data)

class RetrieveTripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ('id', 'latitude_start', 'longitude_start', 'latitude_end', 'longitude_end', 'vehicle', 'passenger')

class UpdateStartTripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ('id', 'latitude_start', 'longitude_start')

    def update(self, instance, validated_data):
        vehicle = instance.vehicle
        vehicle.status = 'on_trip'
        vehicle.save()
        instance.latitude_start = validated_data.get(latitude_start, instance.latitude_start)
        instance.longitude_start = validated_data.get(longitude_start, instance.longitude_start)
        instance.save()
        return instance

class UpdateEndTripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ('id', 'latitude_end', 'longitude_end')

    def update(self, instance, validated_data):
        vehicle = instance.vehicle
        vehicle.status = 'online'
        vehicle.save()
        instance.latitude_end = validated_data.get(latitude_end, instance.latitude_end)
        instance.longitude_end = validated_data.get(longitude_end, instance.longitude_end)
        instance.save()
        return instance
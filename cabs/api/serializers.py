from rest_framework import serializers
from cabs.models import Cab
from accounts.models import Account
from rest_framework.exceptions import PermissionDenied

class ListCabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cab
        fields = ('id', 'latitude', 'longitude', 'status', 'owner')

class CreateCabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cab
        fields = ('id', 'latitude', 'longitude', 'status', 'owner')

    def create(self, validated_data):
        user = validated_data['owner']
        cabs_by_owner = Cab.objects.filter(owner=user.id)
        if cabs_by_owner:
            raise PermissionDenied('A Driver cannot own multiple Cabs.')
        if user.account_type == 'rider':
            raise PermissionDenied('A Rider cannot own a Cab.')
        return Cab.objects.create(**validated_data)

class RetrieveCabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cab
        fields = ('id', 'latitude', 'longitude', 'status', 'owner')

class UpdateCabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cab
        fields = ('id', 'latitude', 'longitude', 'status')


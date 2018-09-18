from rest_framework import serializers
from accounts.models import Account
from django.contrib.auth.hashers import make_password

class ListAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'username', 'account_type')

class CreateAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'username', 'password', 'account_type')

    def create(self, validated_data):
        user = Account.objects.create(
                username=validated_data.get('username'),
                password = make_password(validated_data.get('password')),
                account_type = validated_data.get('account_type')
                )
        return user

class RetrieveAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'username', 'account_type')
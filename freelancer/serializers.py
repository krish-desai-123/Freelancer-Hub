from rest_framework import serializers
from django.db import transaction

from .models import *

class ClientListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ['id','company','employees','description','company_logo','user']

class ClientCreateSerializer(serializers.ModelSerializer):

    first_name = serializers.CharField(max_length=100, write_only=True)
    last_name = serializers.CharField(max_length=100, write_only=True)
    email = serializers.EmailField(max_length=120, write_only=True)
    password = serializers.CharField(max_length=120, write_only=True)

    class Meta:
        model = Client
        fields = ['id','first_name','last_name','email','password','company','employees','description','company_logo']

    def create(self, validated_data):
        with transaction.atomic():

            if User.objects.filter(email=validated_data['email']).exists():
                raise serializers.ValidationError({'email':'Email already exists!'})

            user = User.objects.create_user(
                first_name=validated_data.pop('first_name'),
                last_name=validated_data.pop('last_name'),
                email=validated_data.pop('email'),
                password=validated_data.pop('password'),
                type = 'Client'
            )

            client = Client.objects.create(user=user,**validated_data)

            return client
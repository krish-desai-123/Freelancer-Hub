from rest_framework import serializers
from django.db import transaction

from .models import *
from user.models import User


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'






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


class ClientDetailSerializer(serializers.ModelSerializer):

    user = UserDetailSerializer(read_only=True)

    class Meta:
        model = Client
        fields ='__all__'


class ClientUpdateSerializer(serializers.ModelSerializer):

    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    profile_pic = serializers.ImageField(source='user.profile_pic', required=False)

    class Meta:
        model = Client
        fields = ['id','first_name','last_name','profile_pic','company','employees','description','company_logo']

    def update(self, instance,validated_data):
        if validated_data.get('user'):
            user_data = validated_data.pop('user')

            with transaction.atomic():
                user = instance.user
                user.first_name = user_data.get('first_name', user.first_name)
                user.last_name = user_data.get('last_name', user.last_name)
                user.profile_pic = user_data.get('profile_pic', user.profile_pic)
                user.save()

        return super().update(instance,validated_data)

from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'phone_number', 'password']

    def create(self, validated_data):
        role = self.context.get('role')
        user = User.objects.create_user(**validated_data)

        if role == 'patient':
            user.is_patient = True
        elif role == 'doctor':
            user.is_doctor = True
        elif role == 'pharmacist':
            user.is_pharmacist = True

        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(email=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError("Invalid login credentials")
        if not user.is_active:
            raise serializers.ValidationError("User account is disabled")
        return user

from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        name=CustomUser
        fields=["id","first_name","last_name","email","phone_no","date_of_birth","user_name"]
        extra_kwargs={
            'password':{"write_only":True}
        }

    def create(self,validated_data):
        user=CustomUser.objects.create_user(**validated_data)

        return user
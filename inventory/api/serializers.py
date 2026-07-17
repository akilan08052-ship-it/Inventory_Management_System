from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=["id","first_name","last_name","email","phone_no","date_of_birth","user_name","password"]
        extra_kwargs={
            'password':{"write_only":True}
        }

    def create(self,validated_data):
        print("serial is called")
        print(validated_data)
        user=CustomUser.objects.create_user(**validated_data)

        return user
class SupplierRegisterSerializer(serializers.ModelSerializer):
    company_name=serializers.CharField()
    gst_number=serializers.CharField()
    address=serializers.CharField()
    city=serializers.CharField()
    state=serializers.CharField()
    
    password=serializers.CharField(write_only=True)

    class Meta:
        model=CustomUser
        fields=[
            "first_name",
            "last_name",
            "email",
            "phone_no",
            "password"
            "date_of_birth",
            "company_name",
            "get_number",
            "address",
            "city",
            "state"
        ]
    def create(self,validated_data):
        company_name=validated_data.pop("company_name")
        gst_number=validated_data.pop("gst_number")
        address=validated_data.pop("address")
        city=validated_data.pop("city")
        state=validated_data.pop("state")

        user=CustomUser.objects.create_user(
            **validated_data,
            role="supplier"

        )

        Supplier.objects.create(
            user=user,
            company_name=company_name,
            gst_number=gst_number,
            address=address,
            city=city,
            state=state
        )
        return user

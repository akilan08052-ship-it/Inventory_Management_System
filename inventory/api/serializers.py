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
    
    city=serializers.CharField()
    state=serializers.CharField()
    
    password=serializers.CharField(write_only=True)

    class Meta:
        model=CustomUser
        fields=[
            "first_name",
            "last_name",
            "email",
            "user_name",
            "phone_no",
            "password",
            "date_of_birth",
            "company_name",
            "gst_number",
            "city",
            "state",
            
        ]
    
    def create(self,validated_data):
        company_name=validated_data.pop("company_name")
        gst_number=validated_data.pop("gst_number")
        
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
            city=city,
            state=state
        )
        return user
class Supplierserializer(serializers.ModelSerializer):
    class Meta:
        model=Supplier
        fields=["id","supplier_name","email","user","company_name","dob","phone_number"]
class UnitSeralizer(serializers.ModelSerializer):
    class Meta:
        model=Unit
        fields="__all__"

class CatogerySerializer(serializers.ModelSerializer):
    class Meta:
        model=Catogery
        fields="__all__"
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields="__all__"

class   PurschaseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Purchase
        fields="__all__"
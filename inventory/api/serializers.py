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
class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model=Supplier
        fields=["id","user","supplier_name","company_name","gst_number","dob","email","city","state","phone_number"]
        
class MangerSerializer(serializers.ModelSerializer):
    class Meta:
        models=Manager
        fields=["id","manager","address","udai_no"]
        
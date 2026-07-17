from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.tokens import RefreshToken

#serializer
from .serializers import *
from .models import *

# Create your views here.
@api_view(['POST'])
def register(request):
    if request.method=='POST':
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message':'Account Created'

            },status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['POST'])
def user_in(request):
    if request.method=='POST':
        
        
        email=request.data.get("email")
        password=request.data.get("password")
        print(password)
        
        email_exist=CustomUser.objects.filter(email=email).exists()
        if email_exist:
            user=authenticate(request,email=email,password=password)
            print(user)
            if user is None:
                return Response({"message":"password incorrect"})
            refresh=RefreshToken.for_user(user)
            return Response(
                {"message":"login succesfully",
                 "access":str(refresh.access_token),
                 "refresh":str(refresh)
                },status=status.HTTP_200_OK)
        
        else:
            return Response({"message":"email has no account"},status=status.HTTP_401_UNAUTHORIZED)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
@api_view(['POST'])
@permission_classes([IsAuthenticated]) 
def logout(request):
    if request.method=='POST':
        refresh=request.data.get("refresh")

        token=RefreshToken(refresh)
        token.blacklist()
        return Response({"message":"logout success"},status=status.HTTP_200_OK)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
@api_view(['POST'])
def register_supplier(request):
    if request.method=='POST':
        serializer=SupplierRegisterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Supplier registerd Successfully"},status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
def view_supplier(request):
    if request.method=='GET':
        supplier=Supplier.objects.values("user_name","email")
        return Response(supplier,status=status.HTTP_200_OK)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
@api_view(['POST'])
def add_catogery(request):
    if request.method=='POST':
        serializer=CatogerySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"added Success"},status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
@api_view(['POST'])
def add_unit(request):
    if request.method=='POST':
        serializer=UnitSeralizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Unit Added"},status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST'])
def add_product(request):
    if request.method=='POST':
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"product add successfully"},status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
@api_view(['POST'])
def register_purchase(request):
    if request.method=='POST':
        serializer=PurschaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Purchased Succesfully"})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


                     



        




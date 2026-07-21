from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.tokens import RefreshToken

#serializer
from .serializers import *
from .models import *

# Create your views here.
#admin_view
@api_view(['POST'])
def login(request):
    if request.method=='POST':
        email=request.data.get("email")
        password=request.data.get("password")
        print(password)

        user_exist=CustomUser.objects.filter(email=email).exists()
        print(user_exist)
        if user_exist:
            user=authenticate(email=email,password=password)
            print(user)
            refresh=RefreshToken.for_user(user)
            message={
                
                "email":email,
                "access_token":str(refresh.access_token),
                "refresh_token":str(refresh)

            }
            return Response(message,status=status.HTTP_200_OK)
        else:
            return Response({"message":"user not found"},status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['POST'])
@permission_classes([IsAuthenticated,IsAdminUser])
def register_user(request):
    if request.method=='POST':
        serializer=UserSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"User Created Successfully"},status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['POST','GET'])
@permission_classes([IsAdminUser,IsAuthenticated])
def add_supplier(request):
    if request.method=='GET':
        user=CustomUser.objects.filter(is_staff=False).values("id","email")
        return Response(user,status=status.HTTP_200_OK)
    
    elif request.method=='POST':
        serializer=SupplierSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message":"User is now Supplier"
                },
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
@api_view(['PATCH','GET'])
@permission_classes([IsAdminUser,IsAuthenticated])
def update_Supplier(request,pk):
    if request.method=='PATCH':
        try:
            supplier=Supplier.objects.get(pk=pk)
        except Supplier.DoesNotExist:
            return Response({
                "message":"Supplier not found"
            },status=status.HTTP_404_NOT_FOUND)
        serializer=SupplierSerializer(supplier,data=request.data,partial=True)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            
            
            return Response({"message":"Updated  Successfully"},status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='GET':
        supplier=Supplier.objects.all().values("id","user")
        return Response(supplier,status=status.HTTP_200_OK)
    

    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
@api_view(['DELETE'])
def delete_supplier(request,pk):
    if request.method=='DELETE':
        try:
            supplier=Supplier.objects.get(pk=pk)
        except Supplier.DoesNotExist:
            return Response({"message":"supplier not found"},status=status.HTTP_204_NO_CONTENT)
        supplier.delete()
        return Response({"message":"supplier deleted"})
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


#Register Staff and Manager
@api_view(['POST','GET'])
@permission_classes([IsAuthenticated,IsAdminUser])
def register_manager(request):
    if request.method=='POST':
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"staff added successfully"}) 
        else:
            return Response(serializer.errors,status=status.HTTP_201_CREATED)
    elif request.method=='GET':
        user=CustomUser.objects.filter(is_staff=True).values("id","email")
        return Response(user,status=status.HTTP_200_OK)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['PATCH','GET'])
@permission_classes([IsAuthenticated,IsAdminUser])
def update_manager(request,pk):
    if request.method=='PATCH':
        serializer=MangerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"User is now Manger"},status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
   
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    


    



                     



        




from django.shortcuts import render
from rest_framework.views import APIView
from . serializers import Vehcleserializers,Driveserializers
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from . models import Vehcles,Driver

class VehcleCreateApi(APIView):
    def get(self,request):
        vehcle=Vehcles.objects.all()
        serializer=Vehcleserializers(vehcle,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=Vehcleserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class VehcleDetailApiview(APIView):
    def get_object(self,pk):
        try:
            return Vehcles.objects.get(pk=pk)
        except Vehcles.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        vehcle=self.get_object(pk)
        serializer=Vehcleserializers(vehcle)
        return Response(serializer.data)


    def put(self,request,pk):
        vehcle=self.get_object(pk)
        serializer=Vehcleserializers(vehcle,data=request.data)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
       


    def delete(self,request,pk):
        vehcle=self.get_object(pk)
        vehcle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        


class DriverApi(APIView):
    def get (self,request):
        drivers=Driver.objects.all()
        serializer=Driveserializers(drivers,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=Driveserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class Driverdetails(APIView):
    def get_object(self,pk):
        try:
            return Driver.objects.get(pk=pk)
        except Driver.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        driver=self.get_object(pk)
        serializer=Driveserializers(driver)
        return Response(serializer.data)
    
    def put(self,request,pk):
        driver=self.get_object(pk)
        serializer=Driveserializers(driver,data=request.data)
        if  serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        
    def delete(self,request,pk):
        driver=self.get_object(pk)
        driver.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        

        

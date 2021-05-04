from django.shortcuts import render

#imports for api view 
#api view, rest-framework respose
from rest_framework.decorators import api_view
from rest_framework.response import Response

#imports for serialization
from rest_framework import serializers

#importing model for serialiazation of data
from .models import Supplies
 
 
#creating serializer
class SuppliesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplies    #model to serialize
        fields = '__all__'  #fields in model t serialize


# Create your views here.

#overview of api url navigations
@api_view(['GET'])  #deorator allows only get call for this view
def api_nav(request):
    api_urls_overview = {
        'create': '/api/add-supplies/',
        'read': '/api/view-supplies/',
        'update': '/api/update-supplies/<int:id>',
        'delete': '/api/delete-supplies/<int:id>',
    }
    return Response(api_urls_overview)

#add supplies to the api
@api_view(['POST']) #Post api view decorator for adding supplies
def add_supplies(request):
    #request for user data
    entered_data = request.data
    
    #add user entered data to model
    serializer_obj = SuppliesSerializer(data=entered_data)
    
    #check if data is valid, if true save
    if serializer_obj.is_valid():
        serializer_obj.save()

    return Response(serializer_obj.data)

#view supplies
@api_view(['GET'])
def view_supplies(request):
    #creating View_supplies objects and pass it to SuppliesSerializer class
    view_supplies = Supplies.objects.all()
    serializer_obj = SuppliesSerializer(view_supplies, many=True)
    
    return Response(serializer_obj.data)

@api_view(['POST'])
def update_supplies(request, pk):
    #get instance to be updates
    update_supplies = Supplies.objects.get(id=pk)
    #get value to be updated
    entered_data = request.data
    
    #override instance and data os suppliesserializer class
    serializer_obj = SuppliesSerializer(instance=update_supplies, data=entered_data)
    
    if serializer_obj.is_valid():
        serializer_obj.save()

    return Response(serializer_obj.data)
    
    
@api_view(['DELETE'])
def delete_supplies(request, pk):
    del_supplies = Supplies.objects.get(id=pk)
    del_supplies.delete()
    
    return Response("Item deleted!")
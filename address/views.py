from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Flat
from .models import Hostel
from .models import House

from .serializers import FlatSerializer
from .serializers import HostelSerializer
from .serializers import HouseSerializer


@api_view(['GET','PUT','DELETE'])
def address_detail(request):
    
    if request.method == 'GET':
        	address_detail = Flat.objects.filter(user=request.user)
		Flat_serializer = FlatSerializer(address_detail, many=True)
        	address_detail = House.objects.filter(user=request.user)
  		House_serializer = HouseSerializer(address_detail, many=True)
        	address_detail = Hostel.objects.filter(user=request.user)
		Hostel_serializer = HostelSerializer(address_detail, many=True)
    		return Response(Flat_serializer.data + House_serializer.data + Hostel_serializer.data)

    elif request.method == 'PUT':
	flat_type = request.DATA['flat_type']
        if flat_type == 'Flat':
        	serializer = FlatSerializer(data=request.DATA)
		return serializer_valid(serializer)	
        elif flat_type == 'House':
		serializer = HouseSerializer(data=request.DATA)
		print 
		return serializer_valid(serializer)	
        elif flat_type == 'Hostel':
        	serializer = HostelSerializer(data=request.DATA)
        	return serializer_valid(serializer)	

    elif request.method == 'DELETE':
 	flat_type = request.DATA['flat_type']
#	if flat_type == 'Flat':
 #       	address_detail = Flat.objects.get(address=address)
#		address_detail.delete()
 #       elif flat_type == 'House':
  #      	address_detail = House.objects.get(address=address)
  #		address_detail.delete()
   #     elif flat_type == 'Hostel':
    #    	address_detail = Hostel.objects.get(address=address)
	#	address_detail.delete()
        #return Response(status=status.HTTP_204_NO_CONTENT)


def serializer_valid(serializer):
        if serializer.is_valid():
           	serializer.save()
            	return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:	
            	return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)


  #  curl -H 'Content-Type: application/json' -X PUT -d '{"user":1,"flat_type":"House","locality":"Amrapali","landmark":"amity university","pincode":201301,"latitude":25,"longitude":50,"name":"Amrapali","house_num":"1204A"}' http://127.0.0.1:8000/address/address_detail 

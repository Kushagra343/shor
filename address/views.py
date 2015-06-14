from rest_framework import generics

from .models import Address
from .models import Attributes

from .serializers import AddressSerializer
from .serializers import AttributesSerializer

class AddressList(generics.ListCreateAPIView):
	queryset = Address.objects.all()
        serializer_class = AddressSerializer

class AddressListDetail(generics.RetrieveUpdateDestroyAPIView):
        queryset = Address.objects.all()
        serializer_class = AddressSerializer	
   
class AttributesList(generics.ListCreateAPIView):
	queryset = Attributes.objects.all()
        serializer_class = AttributesSerializer

class AttributesListDetail(generics.RetrieveUpdateDestroyAPIView):
        queryset = Attributes.objects.all()
        serializer_class = AttributesSerializer	
   

#curl -H 'Content-Type: application/json' -X PUT -d '{"address":"asdasdasd","latitude": 24,"longitude": 25}' http://127.0.0.1:8000/address/address/ 

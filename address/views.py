from rest_framework import generics

from .models import Address
from .models import Address_detail

from .serializers import AddressSerializer
from .serializers import AddressDetailSerializer

class AddressList(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class AddressDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer



#curl -H 'Content-Type: application/json' -X PUT -d '{"address":"asdasdasd","latitude": 24,"longitude": 25}' http://127.0.0.1:8000/address/address/

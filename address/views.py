from rest_framework import generics

from .models import Address
from .models import Attributes

from .serializers import AddressSerializer
from .serializers import AttributesSerializer

from .helpers import coordinate_details

class AddressList(generics.ListCreateAPIView):
    """
        curl -H 'Content-Type: application/json' -X PUT -d
        '{"address":"asdasdasd","latitude": 24,"longitude": 25}' http://127.0.0.1:8000/address/address/
    """
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def perform_create(self, serializer):
        if not is_object_exist(instance.address):   
            instance = serializer.save()
        coordinate_details(instance)        

    def is_object_exist(address):
        if Address.objects.filter(address=address).count():
            return True
        return False


class AddressListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class AttributesList(generics.ListCreateAPIView):
    queryset = Attributes.objects.all()
    serializer_class = AttributesSerializer


class AttributesListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attributes.objects.all()
    serializer_class = AttributesSerializer

from rest_framework import generics

from .models import Address
from .models import Attributes

from .serializers import AddressSerializer
from .serializers import AttributesSerializer

from .helpers import attribute_details

class AddressList(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        for i in attribute_details(instance):
            Attributes.objects.create(address=instance,key=i['types'][0],value=i['long_name'])


class AddressListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class AttributesList(generics.ListCreateAPIView):
    queryset = Attributes.objects.all()
    serializer_class = AttributesSerializer


class AttributesListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attributes.objects.all()
    serializer_class = AttributesSerializer

from rest_framework import serializers
from .models import Address
from .models import Address_detail


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ('address', 'latitude','longitude')


class AddressDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address_detail
        fields = ('address','property_type','attributes')




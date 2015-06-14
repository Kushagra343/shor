from rest_framework import serializers
from .models import Address
from .models import Attributes


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ('id', 'address', 'long_position', 'lat_position')


class AttributesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attributes
        fields = ('id', 'address', 'key', 'value')

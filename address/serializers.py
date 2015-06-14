from rest_framework import serializers
from .models import Address
from .models import Attributes


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ('address', 'latitude','longitude')


class AttributesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attributes
        fields = ('address','key','value')




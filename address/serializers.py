from rest_framework import serializers
from .models import Flat
from .models import House
from .models import Hostel


class FlatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Flat
        fields = ('user', 'flat_type', 'locality','landmark','pincode','latitude','longitude','name','block','floor','room_num')


class HostelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hostel
        fields = ('user', 'flat_type', 'locality','landmark','pincode','latitude','longitude','name','floor','room_num')


class HouseSerializer(serializers.ModelSerializer):

    class Meta:
        model = House
        fields = ('user', 'flat_type', 'locality','landmark','pincode','latitude','longitude','name','house_num')



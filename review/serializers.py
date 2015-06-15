from rest_framework import serializers
from .models import Review
from .models import Attributes


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('id', 'address', 'user', 'verified_by')


class AttributesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attributes
        fields = ('id', 'review', 'key', 'value')
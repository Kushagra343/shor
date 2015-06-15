from rest_framework import generics

from .models import Review
from .models import Attributes

from .serializers import ReviewSerializer
from .serializers import AttributesSerializer

#from .helpers import attribute_details

class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        #for i in attribute_details(instance):
        Attributes.objects.create(review=instance,key='',value='')


class ReviewListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class AttributesList(generics.ListCreateAPIView):
    queryset = Attributes.objects.all()
    serializer_class = AttributesSerializer


class AttributesListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attributes.objects.all()
    serializer_class = AttributesSerializer
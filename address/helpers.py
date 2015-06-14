import json
import urllib2

from .models import Address
from .models import Attributes


def coordinate_details(instance):
    latlon = str(instance.long_position) + "," + str(instance.lat_position)
    url = ("https://maps.googleapis.com/maps/api/geocode/json?latlng=" + latlon + "&sensor=true")
    usock = urllib2.urlopen(url)
    data = json.loads(usock.read())
    usock.close()	
    for i in data['results'][1]['address_components']:
		Attributes.objects.create(address=instance,key=i['types'][0],value=i['long_name'])
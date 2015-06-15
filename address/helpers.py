import json
import urllib2

from .models import Address

def attribute_details(instance):
    latlon = str(instance.long_position) + "," + str(instance.lat_position)
    url = ("https://maps.googleapis.com/maps/api/geocode/json?latlng=" + latlon + "&sensor=true")
    usock = urllib2.urlopen(url)
    data = json.loads(usock.read())
    usock.close()	
    return data['results'][1]['address_components']

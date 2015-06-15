import json
from rest_framework import status
from rest_framework.test import APITestCase


address_url = '/address/address/'
address_data = {
        "id": 1,
        "address": "Some Random Address",
        "long_position": "28.376804",
        "lat_position": "78.640811",
}
attribute_url = '/address/attributes/'
attribute_data = {
        "id": 6,
        "address": 1,
        "key": "28.376804",
        "value": "78.640811",
}



class AddressTestCase(APITestCase):
    

    def test_create_address(self):
        address = self.client.post(address_url, address_data, format='json')
        self.assertEqual(address.status_code, status.HTTP_201_CREATED)
        self.assertEqual(address.data, address_data)

    def test_get_address(self):
    	address = self.client.post(address_url, address_data, format='json')
        request = self.client.get('/address/address/1/')
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_get_address_list(self):
        request = self.client.get(address_url)
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_delete_address(self):
        address = self.client.post(address_url,address_data, format='json')
        request = self.client.delete('/address/address/1/')
        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)
    


class AttributesTestCase(APITestCase):

    def test_create_address_attribute(self):
        address = self.client.post(address_url, address_data, format='json')
        request = self.client.get(attribute_url)
        self.assertEqual(address.status_code, status.HTTP_201_CREATED)
        self.assertEqual(address.data, address_data)
        self.assertNotEqual(len(request.data) , 0) 

    def test_create_attribute(self):
        address = self.client.post(address_url,address_data, format='json')
        attribute = self.client.post(attribute_url,attribute_data, format='json')
        self.assertEqual(attribute.status_code, status.HTTP_201_CREATED)
        self.assertEqual(attribute.data,attribute_data)

    def test_get_attribute(self):
        address = self.client.post(address_url, address_data, format='json')
        attribute = self.client.post(attribute_url,attribute_data, format='json')
        request = self.client.get('/address/attributes/1/',attribute_data, format='json')
        self.assertEqual(request.status_code, status.HTTP_200_OK)
   
    def test_delete_attribute(self):
        address = self.client.post(address_url, address_data, format='json')
        attribute = self.client.post(attribute_url,attribute_data, format='json')
        request = self.client.delete('/address/attributes/1/',attribute_data, format='json')
        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)

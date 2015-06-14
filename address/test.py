from rest_framework import status

import json

from rest_framework.test import APITestCase


class AddressTestCase(APITestCase):
    url = '/address/address/'
    data = {
        "id": 1,
        "address": "Some Random Address",
        "long_position": "28.376804",
        "lat_position": "78.640811",
    }

    def test_create_address(self):
        """
        Ensure we can create a new address object.
        """
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, self.data)


    def test_get_address(self):
    	response = self.client.post(self.url, self.data, format='json')
        request = self.client.get('/address/address/1/')
        self.assertEqual(request.status_code, status.HTTP_200_OK)


    def test_get_address_list(self):
        request = self.client.get('/address/address/')
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_delete_address(self):
        response = self.client.post(self.url, self.data, format='json')
        request = self.client.delete('/address/address/1/')
        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)
    


class AttributesTestCase(APITestCase):
    url = '/address/address/'
    data = {
        "id": 1,
        "address": "Some Random Address",
        "long_position": "28.376804",
        "lat_position": "78.640811",
    }
    def test_create_add_attribute(self):
        """
        Ensure we can create a new address object.
        """
        response = self.client.post(self.url, self.data, format='json')
        request = self.client.get('/address/attributes/')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, self.data)
        self.assertNotEqual(len(request.data) , 0) 

    def test_create_attribute(self):

        data = {
        "id": 6,
        "address": 1,
        "key": "28.376804",
        "value": "78.640811",
        }
        address = self.client.post(self.url, self.data, format='json')
        response = self.client.post('/address/attributes/',data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data,data)

    def test_get_attribute(self):

        data = {
        "id": 6,
        "address": 1,
        "key": "28.376804",
        "value": "78.640811",
        }
        address = self.client.post(self.url, self.data, format='json')
        response = self.client.post('/address/attributes/',data, format='json')
        request = self.client.get('/address/attributes/1/',data, format='json')
        self.assertEqual(request.status_code, status.HTTP_200_OK)
   
    def test_delete_attribute(self):
        data = {
        "id": 6,
        "address": 1,
        "key": "28.376804",
        "value": "78.640811",
        }
        address = self.client.post(self.url, self.data, format='json')
        response = self.client.post('/address/attributes/',data, format='json')
        request = self.client.delete('/address/attributes/1/',data, format='json')
        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)


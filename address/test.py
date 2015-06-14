from rest_framework import status

import json

from rest_framework.test import APITestCase


class AddressTestCase(APITestCase):

    def test_create_address(self):
        """
        Ensure we can create a new address object.
        """
        url = '/address/address/'
        data = {
            "id": 1,
            "address": "Some Random Address",
            "long_position": "28.376804",
            "lat_position": "78.640811",
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, data)


    def test_get_address(self):
    	response = self.client.post(url, data, format='json')
        request = self.client.get('/address/address/1/')
        self.assertEqual(request.status_code, status.HTTP_200_OK)


    def test_get_address_list(self):
        request = self.client.get('/address/address/')
        self.assertEqual(request.status_code, status.HTTP_200_OK)


	def test_delete_address(self):
        response = self.client.delete('/address/address/2')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


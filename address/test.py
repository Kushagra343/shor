from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory


class AddressTestCase(APITestCase):

    def test_get_list(self):
        factory = APIRequestFactory()
        request = self.client.get('/address/address/')
        self.assertEqual(request.status_code, status.HTTP_200_OK)

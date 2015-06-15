import json
from rest_framework import status
from rest_framework.test import APITestCase


review_url = '/review/review/'
review_data = {
        "id": 1,
        "user": "kush",
        "address": "Some Random Address",
        "verified_by": False   ,
}
attribute_url = '/review/attributes/'
attribute_data = {
        "id": 2,
        "review": 1,
        "key": "28.376804",
        "value": "78.640811",
}



class ReviewTestCase(APITestCase):
    

    def test_create_review(self):
        review = self.client.post(review_url, review_data, format='json')
        self.assertEqual(review.status_code, status.HTTP_201_CREATED)
        self.assertEqual(review.data, review_data)

    def test_get_review(self):
        review = self.client.post(review_url, review_data, format='json')
        request = self.client.get('/review/review/1/')
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_get_review_list(self):
        request = self.client.get(review_url)
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_delete_review(self):
        review = self.client.post(review_url,review_data, format='json')
        request = self.client.delete('/review/review/1/')
        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)
    


class AttributesTestCase(APITestCase):

    def test_create_review_attribute(self):
        review = self.client.post(review_url, review_data, format='json')
        request = self.client.get(attribute_url)
        self.assertEqual(review.status_code, status.HTTP_201_CREATED)
        self.assertEqual(review.data, review_data)
        self.assertNotEqual(len(request.data) , 0) 

    def test_create_attribute(self):
        review = self.client.post(review_url,review_data, format='json')
        attribute = self.client.post(attribute_url,attribute_data, format='json')
        self.assertEqual(attribute.status_code, status.HTTP_201_CREATED)
        self.assertEqual(attribute.data,attribute_data)

    def test_get_attribute(self):
        review = self.client.post(review_url, review_data, format='json')
        attribute = self.client.post(attribute_url,attribute_data, format='json')
        request = self.client.get('/review/attributes/1/',attribute_data, format='json')
        self.assertEqual(request.status_code, status.HTTP_200_OK)
   
    def test_delete_attribute(self):
        review = self.client.post(review_url, review_data, format='json')
        attribute = self.client.post(attribute_url,attribute_data, format='json')
        request = self.client.delete('/review/attributes/1/',attribute_data, format='json')
        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)
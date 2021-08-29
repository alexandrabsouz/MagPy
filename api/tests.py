from rest_framework import status
from rest_framework.test import APIClient, APITestCase

# Create your tests here.

class ClientTest(APITestCase):
    
    
    url = 'http://127.0.0.1:8000/api/projects/'

    def post(self, payload, url=None):
        """
        Helper to send an HTTP post.

        @param (dict) payload: request body

        @returns: response
        """
        if url is None:
            url = self.url

        return self.client.post(url, payload, format='json')

    def test_response_201(self):
        
        payload =   {
                        "name": "teste2",
                        "packages": [
                            {"name":"django"},
                            {"name":"graphene"}
                        ]
                    } 
        
        response = self.post(payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_response_400(self):
        
        payload =   {
                        "name": "titan",
                        "packages": [
                            {"name": "pypypypypypypypypypypy"},
                            {"name": "graphene", "version": "1900"}
                        ]
                    } 
    
        response = self.post(payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


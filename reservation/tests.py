from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Cinema, Movie, Showtime, Seat, Reservation

class APITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_cinemas(self):
        response = self.client.get('/cinemas/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
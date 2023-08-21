from django.test import TestCase
from .models import Cinema, Movie, Showtime, Seat, Reservation

class IntegrationTestCase(TestCase):
    def test_make_reservation(self):
        cinema = Cinema.objects.create(name="Sample Cinema")
        movie = Movie.objects.create(title="Sample Movie")
        showtime = Showtime.objects.create(cinema=cinema, movie=movie, show_time="2023-08-20T15:00:00Z")
        seat = Seat.objects.create(showtime=showtime, seat_number="A1")

        response = self.client.post('/reservations/', {
            "showtime": showtime.pk,
            "seat": seat.pk,
            "seat_last_modified": seat.last_modified,
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
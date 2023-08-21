from rest_framework import generics, status
from rest_framework.response import Response
from .models import Cinema, Movie, Showtime, Seat, Reservation
from .serializers import CinemaSerializer, MovieSerializer, ShowtimeSerializer, SeatSerializer, ReservationSerializer
from django.db import transaction, IntegrityError
from django.utils import timezone




class CinemaListView(generics.ListAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer


class MovieListView(generics.ListAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        cinema = Cinema.objects.get(pk=self.kwargs['pk'])
        return Movie.objects.filter(showtime__cinema=cinema)


class SeatListView(generics.ListAPIView):
    serializer_class = SeatSerializer

    def get_queryset(self):
        showtime = Showtime.objects.get(pk=self.kwargs['pk'])
        return Seat.objects.filter(showtime=showtime, is_reserved=False)


class ReservationCreateView(generics.CreateAPIView):
    serializer_class = ReservationSerializer

    def create(self, request, *args, **kwargs):
        showtime_id = request.data.get('showtime')
        seat_id = request.data.get('seat')

        try:
            with transaction.atomic():
                showtime = Showtime.objects.select_for_update().get(pk=showtime_id)
                seat = Seat.objects.select_for_update().get(pk=seat_id)

                if seat.is_reserved:
                    return Response({"error": "Seat is already reserved."}, status=status.HTTP_400_BAD_REQUEST)

                client_seat_last_modified = request.data.get('seat_last_modified')

                if client_seat_last_modified:
                    server_seat_last_modified = timezone.make_aware(client_seat_last_modified)
                else:
                    # Set a default value or handle the absence of seat_last_modified as needed
                    server_seat_last_modified = timezone.now()

                if seat.last_modified > server_seat_last_modified:
                    return Response({"error": "Seat information has changed. Please refresh and try again."},
                                    status=status.HTTP_409_CONFLICT)

                reservation = Reservation(showtime=showtime, seat=seat)
                reservation.save()

                seat.is_reserved = True
                seat.last_modified = timezone.now()
                seat.save()

                serializer = self.get_serializer(reservation)
                headers = self.get_success_headers(serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except (Showtime.DoesNotExist, Seat.DoesNotExist, IntegrityError):
            return Response({"error": "Invalid showtime or seat ID."}, status=status.HTTP_400_BAD_REQUEST)

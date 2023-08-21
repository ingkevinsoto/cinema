from django.db import models


class Cinema(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Showtime(models.Model):
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    show_time = models.DateTimeField()

    def __str__(self):
        return f"{self.movie.title} at {self.cinema.name} ({self.show_time})"


class Seat(models.Model):
    showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10)
    is_reserved = models.BooleanField(default=False)
    last_modified = models.DateTimeField(auto_now=True)  # Timestamp to track modifications

    def __str__(self):
        return f"Seat {self.seat_number} ({'Reserved' if self.is_reserved else 'Available'})"


class Reservation(models.Model):
    showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)

    def __str__(self):
        return f"Reservation: {self.seat} for {self.showtime}"

from django.contrib import admin
from .models import Cinema, Movie, Showtime, Seat, Reservation

@admin.register(Cinema)
class CinemaAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Showtime)
class ShowtimeAdmin(admin.ModelAdmin):
    list_display = ('cinema', 'movie', 'show_time')

@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ('showtime', 'seat_number', 'is_reserved')

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('showtime', 'seat')
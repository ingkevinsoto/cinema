# Movie Reservation System

Welcome to the Movie Reservation System README! This document provides an overview of the system architecture, available API endpoints, and instructions for setting up and running the project locally.

## System Architecture

The Movie Reservation System is a Django-based web application that facilitates movie reservations in multiple cinemas. It provides an API for users to interact with the system, including getting information about cinemas, movies, showtimes, seats, and making reservations.

The key components of the system include:
- Django: The web framework used to build the application.
- Django REST framework: A powerful toolkit for building Web APIs in Django.
- SQLite (or your chosen database): Used to persist data including cinemas, movies, showtimes, seats, and reservations.

## API Endpoints

The following API endpoints are available for interaction:

- **GET /cinemas/**:
  - Description: Get a list of all cinemas.
  - Response: List of cinemas with details.

- **GET /cinemas/{cinema_id}/movies/**:
  - Description: Get a list of movies showing in a particular cinema.
  - Response: List of movies available in the specified cinema.

- **GET /showtimes/{showtime_id}/seats/**:
  - Description: Get available seats for a specific movie showing.
  - Response: List of available seats for the specified showtime.

- **POST /reservations/**:
  - Description: Make a reservation for a seat in a specific movie showing.
  - Request Body: `{ "showtime": showtime_id, "seat": seat_id, "seat_last_modified": seat_last_modified }`
  - Response: Reserved seat details.

## Local Setup

Follow these steps to set up the Movie Reservation System locally:

1. Clone the repository:
2. Create a virtual environment and activate it:
3. Install project dependencies:
4. Apply database migrations:
5. Create a superuser for the admin panel:
6. Run the development server:
7. Access the admin panel at http://localhost:8000/admin/ to add cinemas, movies, showtimes, and seats.

8. Use API endpoints to interact with the system.

## Additional Information

- Remember to adjust settings (such as database configurations) in `settings.py` to match your environment.
- Proper error handling, validation, and concurrency control are implemented for reliability.
- Ensure you handle secrets securely. You might want to use environment variables or a secrets manager for sensitive information.

Feel free to explore and extend the system based on your needs. Happy coding!

## Running Tests

To run the unit tests and integration tests for the Movie Reservation System, follow these steps:

1. Ensure you've set up the project locally as mentioned in the setup instructions.

2. Activate your virtual environment if not already activated:
3. Navigate to your project's root directory (where `manage.py` is located).

4. Run the tests using the `test` command:

## Run with Docker
docker-compose build

## Start the Docker containers
docker-compose up

## Run migrations
docker-compose run web python manage.py migrate
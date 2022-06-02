from django.db import models

# Create your models here.


class Agent(models.Model):
    name = models.CharField(max_length=100)
    rating = models.FloatField()

    def __str__(self):
        return self.name


class Airline(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Itinerary(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    price = models.CharField(max_length=50)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)

    def __str__(self):
        return self.id


class Leg(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    departure_airport = models.CharField(max_length=10)
    arrival_airport = models.CharField(max_length=10)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    stops = models.IntegerField()
    airline_id = models.ForeignKey(Airline, on_delete=models.CASCADE)
    duration_mins = models.IntegerField()
    itinerary = models.ForeignKey(
        Itinerary, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.id}: from:{self.departure_airport} - to:{self.arrival_airport}"

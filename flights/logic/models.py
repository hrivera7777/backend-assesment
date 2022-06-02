from django.db import models

# Create your models here.


class Agent(models.Model):
    name = models.CharField(max_length=100)
    rating = models.FloatField()


class Airline(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100)


class Itinerary(models.Model):
    price = models.CharField(max_length=50)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)


class Leg(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    departure_airport = models.CharField(max_length=10)
    arrival_airport = models.CharField(max_length=10)
    departure_time = models.DateField()
    arrival_time = models.DateField()
    stops = models.IntegerField()
    airline_id = models.ForeignKey(Airline, on_delete=models.CASCADE)
    duration_mins = models.IntegerField()
    itinerary = models.ForeignKey(
        Itinerary, on_delete=models.CASCADE, null=True)

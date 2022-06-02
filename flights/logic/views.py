from django.shortcuts import render
import datetime
from django.http import HttpResponse
import json
from .models import Agent, Airline, Itinerary, Leg
# Create your views here.


def PopulateDB(request):
    file_data = open('../data/flights.json')
    flights = json.load(file_data)
    pass

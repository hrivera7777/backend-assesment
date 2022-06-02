from django.shortcuts import render
import datetime
from django.http import HttpResponse
import json
from .models import Agent, Airline, Itinerary, Leg
from django.core import serializers
import copy
# Create your views here.


def PopulateDB():
    file_data = open('../data/flights.json')
    flights = json.load(file_data)
    legs = flights.pop("legs")
    populate_legs(legs)
    itineraries = flights.pop("itineraries")
    populate_itineraries(itineraries)


def flights(request):
    itineraries = Itinerary.objects.all()
    if not itineraries:
        PopulateDB()
    qp = request.GET
    iteneraries = itineraries.values()
    payload = []
    for itinerary in iteneraries:
        itinerary_c = copy.deepcopy(itinerary)
        agent = Agent.objects.get(id=itinerary_c.pop("agent_id"))

        if "agent" in qp.keys():
            itinerary_c = {
                **itinerary_c,
                "agent": {
                    "name": agent.name,
                    "rating": agent.rating
                }
            }
        payload.append(itinerary_c)

    return HttpResponse(payload)


def populate_legs(legs):
    for leg in legs:
        leg_c = copy.deepcopy(leg)
        airline_data = {
            "id": leg_c.pop("airline_id"),
            "name": leg_c.pop("airline_name")
        }
        airline = Airline(**airline_data)
        airline.save()
        leg_c = {
            **leg_c,
            "airline_id": airline
        }
        leg_created = Leg(**leg_c)
        leg_created.save()


def populate_itineraries(itineraries):

    for itinerary in itineraries:
        itinerary_c = copy.deepcopy(itinerary)
        legs = itinerary_c.pop("legs")
        agent_data = {
            "name": itinerary_c.pop("agent"),
            "rating": itinerary_c.pop("agent_rating")
        }
        agent = Agent(**agent_data)
        agent.save()
        itinerary_c = {
            **itinerary_c,
            "agent": agent
        }

        itinerary_created = Itinerary(**itinerary_c)
        itinerary_created.save()

        for leg in legs:
            try:
                leg_found = Leg.objects.get(id=leg)
            except Leg.DoesNotExist:
                continue
            leg_found.itinerary = itinerary_created
            leg_found.save()


def populate_agent():
    pass

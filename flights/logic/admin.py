from django.contrib import admin
from .models import Agent, Leg, Itinerary

# Register your models here.


class AgentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Agent, AgentAdmin)


class LegAdmin(admin.ModelAdmin):

    pass


admin.site.register(Leg, LegAdmin)


class ItineraryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Itinerary, ItineraryAdmin)

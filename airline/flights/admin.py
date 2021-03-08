from django.contrib import admin

from .models import Flight, airport, passenger

# Register your models here.
class flightadmin(admin.ModelAdmin):
	list_display = ("id", "origin", "destination", "duration")

class passengeradmin(admin.ModelAdmin):
	filter_horizontal  = ("flights",)
										

admin.site.register(airport)
admin.site.register(Flight, flightadmin)
admin.site.register(passenger, passengeradmin)

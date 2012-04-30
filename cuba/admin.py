# -*- coding: utf-8 -*-

from django.contrib import admin
from cuba.models.accounts import UserProfile
from cuba.models.activities import Activity
from cuba.models.bookings import Booking, BookingParticipant
from cuba.models.photos import Photo
from cuba.models.videos import Video
from cuba.models.places import Country, City

admin.site.register(UserProfile)
admin.site.register(Activity)
admin.site.register(Booking)
admin.site.register(BookingParticipant)
admin.site.register(Photo)
admin.site.register(Video)
admin.site.register(Country)
admin.site.register(City)


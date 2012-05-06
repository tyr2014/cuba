# -*- coding: utf-8 -*-

from django.contrib import admin
from cuba.models.accounts import UserProfile
from cuba.models.activities import Activity, Coupon
from cuba.models.generics import Category, CancelPolicy, TaggedItem
from cuba.models.orders import Order, OrderParticipant
from cuba.models.photos import Photo
from cuba.models.ratings import Rating, RatingEntry
from cuba.models.videos import Video
from cuba.models.places import Country, City

admin.site.register(Activity)
admin.site.register(Category)
admin.site.register(CancelPolicy)
admin.site.register(City)
admin.site.register(Country)
admin.site.register(Coupon)
admin.site.register(Order)
admin.site.register(OrderParticipant)
admin.site.register(Photo)
admin.site.register(Rating)
admin.site.register(RatingEntry)
admin.site.register(TaggedItem)
admin.site.register(UserProfile)
admin.site.register(Video)


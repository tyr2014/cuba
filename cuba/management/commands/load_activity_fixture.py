# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import timedelta
import random
from cuba.models import User
from django.core.management.base import BaseCommand
import json
from django.utils.datetime_safe import datetime
from cuba.models.accounts import UserProfile
from cuba.models.activities import Activity
from cuba.models.generics import Category, CancelPolicy
from cuba.models.photos import Photo
from cuba.utils.alias import pinyinize
from cuba.utils.storages import ExtendedFile

class Command(BaseCommand):
  categories = Category.objects.all()
  policies = CancelPolicy.objects.all()

  def process_author(self, item):
    try:
      name = item['details']['发起人']
    except Exception:
      # return a user which exists
      return User.objects.get(pk=1)
    last_name = name[0]
    first_name = name[1:]
    username = pinyinize(name)
    user, created = User.objects.get_or_create(last_name=last_name, first_name=first_name, username=username)
    if created:
      # provide dummy password
      user.set_password('123456')
      profile = UserProfile(user=user, slug=user.pk)
      profile.save()
      user.save()
    return user

  def process_activity(self, item, user):
    import urllib2
    photos = []

    for url in item['images']:
      photo = Photo()
      photo.author = user
      photo.filename = ExtendedFile(urllib2.urlopen(url))
      photo.save()
      photos.append(photo)

    if not photos:
      print 'Activity %s has no images, skip.' % item['title']
      return

    if Activity.objects.filter(title=item['title']).exists():
      print 'Activity %s has been created already.' % item['title']
      return

    a = Activity()
    a.city_id = 1
    a.country_id = 1
    a.title = item['title']
    a.author = user
    a.description = item['description'][:50]
    a.activity_info = item['description']
    a.crawl_url = item['id']
    a.publish_date = datetime.now() + timedelta(days=random.randrange(0, 10))
    a.expiry_date = a.publish_date + timedelta(days=random.randrange(3, 14))
    a.start = a.expiry_date + timedelta(days=random.randrange(1, 7))
    a.end = a.start + timedelta(days=random.randrange(1,14))
    a.market_cost = random.randrange(100, 1000, 50)
    a.cost = a.market_cost * random.randrange(40, 80, 5) / 100
    a.min_participants = random.randrange(2, 15)
    a.max_participants = a.min_participants + random.randrange(0, 15)
    a.cancel_policy = random.choice(self.policies)
    a.cover = photos[0]
    a.save()

    # process m2m fields
    a.category.add(random.choice(self.categories))
    for photo in photos:
      a.photo_set.add(photo)
    a.save()
    print 'Activity %s processed' % a.title


  def handle(self, filename, *args, **options):
    items = json.load(open(filename))
    for item in items:
      user = self.process_author(item)
      self.process_activity(item, user)
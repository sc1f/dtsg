from django.db import models
from django.contrib import admin
from datetime import date
from django.utils import timezone

class Election(models.Model):
    name = models.CharField(default="Election",max_length=200)
    year = models.PositiveSmallIntegerField(primary_key=True)
    election_date = models.DateField()
    description = models.TextField()

    def has_passed(self):
        return date.today() > self.election_date

    def __str__(self):
        return str(self.year)

class ElectionAdmin(admin.ModelAdmin):
    list_display = ("year", "election_date")

class Race(models.Model):
    name = models.CharField(max_length=200)
    year = models.ForeignKey('Election', on_delete=models.CASCADE,)
    description = models.TextField()

    def __str__(self):
        return self.name

class RaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'year')
    list_filter = ['year']

class Position(models.Model):
    name = models.CharField(max_length=200)
    race = models.ForeignKey('Race', on_delete=models.CASCADE,)
    position_year = models.ForeignKey('Election', on_delete=models.CASCADE,)
    positions_available = models.PositiveSmallIntegerField(unique=False)
    order = models.PositiveSmallIntegerField(unique=False,blank=True)

    def __str__(self):
        return self.name

class PositionAdmin(admin.ModelAdmin):
    list_display = ('name', 'position_year', 'race', 'positions_available')
    list_filter = ('race', 'position_year')

class Candidate(models.Model):
    name = models.CharField(max_length=200)
    position = models.ForeignKey('Position', on_delete=models.CASCADE,)
    major = models.CharField(max_length=200, unique=False)
    year = models.CharField(max_length=200, unique=False)
    image = models.FileField(upload_to='images/%Y/candidates/', blank=True, null=True)
    image_credit = models.CharField(max_length=200, blank=True, unique=False)

    #information
    statement = models.TextField()
    platform = models.TextField()

    #contact
    website = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    winner = models.BooleanField()

    #results
    votes_received = models.PositiveSmallIntegerField(blank=True, null=True, unique=False)
    total_votes= models.PositiveSmallIntegerField(blank=True, null=True, unique=False)

    #publish
    published = models.BooleanField(default=False)

    def percentage_of_votes(self):
        percent = (self.votes_received / self.total_votes) * 100
        return str(percent + "%")

    def __str__(self):
        return self.name
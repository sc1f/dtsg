from django.db import models
from django.contrib import admin

class Election(models.Model):
    name = models.CharField(default="Election",max_length=200)
    year = models.PositiveSmallIntegerField(primary_key=True)
    description = models.TextField()

    def __str__(self):
        return str(self.year)

class Race(models.Model):
    name = models.CharField(max_length=200)
    year = models.ForeignKey('Election', on_delete=models.CASCADE,)
    description = models.TextField()

    def __str__(self):
        return self.name

class RaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'year')

class Candidate(models.Model):
    #profile
    name = models.CharField(max_length=200)
    race = models.ForeignKey('Race', on_delete=models.CASCADE,)
    major = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    image = models.FileField(upload_to='images/%Y/candidates/', blank=True, null=True)
    image_credit = models.CharField(max_length=200, blank=True)

    #information
    statement = models.TextField()
    platform = models.TextField()

    #contact
    website = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    winner = models.BooleanField()

    def __str__(self):
        return self.name

class CandidateAdmin(admin.ModelAdmin):
    list_display = ("name", "race", "winner")
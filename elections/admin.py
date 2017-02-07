from django.contrib import admin
from .models import Election, Race, Candidate, RaceAdmin, CandidateAdmin

# Register your models here.
admin.site.register(Election)
admin.site.register(Race, RaceAdmin)
admin.site.register(Candidate, CandidateAdmin)
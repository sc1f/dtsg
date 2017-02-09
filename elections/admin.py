from django.contrib import admin
from .models import Election, Race, Position, Candidate, RaceAdmin, CandidateAdmin, PositionAdmin

# Register your models here.
admin.site.register(Election)
admin.site.register(Race, RaceAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Candidate, CandidateAdmin)

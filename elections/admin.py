from django.contrib import admin
from .models import Election, Race, Position, Candidate, RaceAdmin, PositionAdmin
admin.site.site_header = 'Daily Texan Student Government Explorer - Admin Panel'

# Allows us to bulk publish candidates

class CandidateAdmin(admin.ModelAdmin):
    list_display = ("name", "position", "winner", "published")
    list_filter = ('position', 'winner', 'published')
    actions = ["publish_candidate", "unpublish_candidate"]

    def publish_candidate(self, request, queryset):
        rows_updated = queryset.update(published=True)
        if rows_updated == 1:
            message_bit = "1 candidate was"
        else:
            message_bit = "%s candidates were" % rows_updated
        self.message_user(request, "%s published." % message_bit)
    publish_candidate.short_description = "Publish selected candidates"

    def unpublish_candidate(self, request, queryset):
        rows_unpublished = queryset.update(published=False)
        if rows_unpublished == 1:
            message_bit = "1 candidate was"
        else:
            message_bit = "%s candidates were" % rows_unpublished
        self.message_user(request, "%s published." % message_bit)
    unpublish_candidate.short_description = "Unpublish selected candidates"


# Register your models here.
admin.site.register(Election)
admin.site.register(Race, RaceAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Candidate, CandidateAdmin)

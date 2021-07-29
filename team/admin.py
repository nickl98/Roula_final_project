from django.contrib import admin

from .models import Team
# Register Team Model here.


class TeamAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'college',
        'years_experience',
        'image',
        )
    ordering = ('name',)


admin.site.register(Team, TeamAdmin)


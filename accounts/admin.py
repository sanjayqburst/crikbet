from django.contrib import admin

from core.models import MatchPlayer, Matches, Players, Teams, UserMatchPlayer, UserMatches

# Register your models here.
admin.site.register(Teams)
admin.site.register(Players)
admin.site.register(Matches)
admin.site.register(MatchPlayer)
admin.site.register(UserMatches)
admin.site.register(UserMatchPlayer)
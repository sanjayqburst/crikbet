from .models import Matches


class MatchService:
    def get_matches(self):
        return Matches.objects.all()
        
from rest_framework.response import Response
from rest_framework.views import APIView

from team.serializers import TeamSerializer
from .models import Teams
# Create your views here.
class TeamView(APIView):

    def get(self,request):
        teams=Teams.objects.all()
        serializers=TeamSerializer(teams,many=True)
        return Response(serializers.data)

    def post(self,request):
        data=request.data
        serializers=TeamSerializer(data=data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data)
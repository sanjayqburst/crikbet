from rest_framework.response import Response
from rest_framework.views import APIView
from .models import MatchPlayer
from .serializers import MatchPlayerSerializer

# Create your views here.

class MatchPlayerView(APIView):
    """
    Method for API call for match palyer selection GET and POST requests. 
    """
    def get(self,request):
        matchplayer=MatchPlayer.objects.all()
        serializer=MatchPlayerSerializer(matchplayer,many=True)
        return Response(serializer.data)

    def post(self,request):
        data=request.data
        serializers=MatchPlayerSerializer(data=data)
        serializers.is_valid()
        serializers.save()
        return Response(serializers.data)
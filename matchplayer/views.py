from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from .services import matchplayerobjects
from .serializers import MatchPlayerSerializer

# Create your views here.

class MatchPlayerView(APIView):
    """
    Method for API call for match palyer selection GET and POST requests. 
    """
    def get(self,request):
        """
        Query all the matchplayer objects and send as response

        :param request Request object
        :return : Response JSON data 
        """
        matchplayer=matchplayerobjects
        serializer=MatchPlayerSerializer(matchplayer,many=True)
        return Response(serializer.data)

    def post(self,request):
        """
        Creates new matchplayer object

        :param request: Request Object
        :return: Response JSON data        
        """
        data=request.data
        serializers=MatchPlayerSerializer(data=data)
        serializers.is_valid()
        serializers.save()
        return Response(serializers.data)
from rest_framework.response import Response
from rest_framework.views import APIView
from match.serializers import MatchSerializer
from .models import Matches
from .services import MatchService
# Create your views here.
class MatchView(APIView):
    """
    View for handling requests about match data.
    """

    def get(self,request):
        """
        Query all the match objects and send as response

        :param request Request object
        :return : Response JSON data 
        """
        serializer=MatchSerializer(MatchService().get_matches(),many=True)
        return Response(serializer.data)

    def post(self,request):
        """
        Creates new match object

        :param request: Request Object
        :return: Response JSON data        
        """
        data=request.data
        serializers=MatchSerializer(data=data)
        serializers.is_valid()
        serializers.save()
        return Response(serializers.data)

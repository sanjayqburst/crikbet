from rest_framework.response import Response
from player.serializers import PlayerSerializer
from .models import Players
from .services import playerobject
from rest_framework.views import APIView


# Create your views here.
class PlayerView(APIView):
    """ 
    Method for creation of API view for player information.
    """
    def get(self,request):
        """
        Query all the player objects and send as response data

        :param request Request object
        :return : Response JSON data 
        """
        player=playerobject
        serializers=PlayerSerializer(player, many=True)
        return Response(serializers.data)

    def post(self,request):
        """
        Creates new player object

        :param request: Request Object
        :return: Response JSON data        
        """
        data=request.data
        serializers=PlayerSerializer(data=data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data)
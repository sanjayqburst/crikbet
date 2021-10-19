from rest_framework.response import Response
from rest_framework.views import APIView
from .services import teamobject
from team.serializers import TeamSerializer
from .models import Teams
# Create your views here.


class TeamView(APIView):
    """ 
    Method for handling API view for team.
    """
    def get(self,request):
        """
        Query all the team objects and send as response data

        :param request Request object
        :return : Response JSON data 
        """
        teams=teamobject
        serializers=TeamSerializer(teams,many=True)
        return Response(serializers.data)

    def post(self,request):
        """
        Creates new team object

        :param request: Request Object
        :return: Response JSON data        
        """
        data=request.data
        serializers=TeamSerializer(data=data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data)
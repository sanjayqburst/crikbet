from rest_framework.views import APIView
from rest_framework.response import Response
from .services import usermatchplayerobjects
from .serializers import UserMatchPlayerSerializer
import json
# Create your views here.


class UserMatchPlayerView(APIView):
    """
    Method for handling GET and POST request on UserMatchPlayer model.
    """
    def get(self,request):
        """
        Query all the usermatchplayer objects and send as response

        :param request Request object
        :return : Response JSON data 
        """
        usermatchplayer=usermatchplayerobjects
        serializer=UserMatchPlayerSerializer(usermatchplayer,many=True)
        return Response(serializer.data)

    def post(self,request):
        """
        Creates new usermatchplayer object
        checks if data is send in and dictionary format and conver to json data.

        :param request: Request Object
        :return: Response JSON data        
        """
        data=request.data
        if 'data' in data:
            data=json.loads(data['data'])
        serializers=UserMatchPlayerSerializer(data=data,many=True)
        serializers.is_valid()
        serializers.save()
        return Response(serializers.data)

from rest_framework.views import APIView
from rest_framework.response import Response
from .services import usermatchobjects
from .serializers import UserMatchSerializer
# Create your views here.


class UserMatchView(APIView):
    """ 
    Method for handling GET and POST request of user match model.
    """
    def get(self,request):
        """
        Query all the usermatch objects and send as response

        :param request Request object
        :return : Response JSON data 
        """
        usermatch=usermatchobjects
        serializer=UserMatchSerializer(usermatch,many=True)
        return Response(serializer.data)

    def post(self,request):
        """
        Creates new usermatch object

        :param request: Request Object
        :return: Response JSON data        
        """
        data=request.data
        serializers=UserMatchSerializer(data=data)
        serializers.is_valid()
        serializers.save()
        return Response(serializers.data)
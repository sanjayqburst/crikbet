from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserMatches
from .serializers import UserMatchSerializer
# Create your views here.


class UserMatchView(APIView):
    """ 
    Method for handling GET and POST request of user match model.
    """
    def get(self,request):
        usermatch=UserMatches.objects.all()
        serializer=UserMatchSerializer(usermatch,many=True)
        return Response(serializer.data)

    def post(self,request):
        data=request.data
        serializers=UserMatchSerializer(data=data)
        serializers.is_valid()
        serializers.save()
        return Response(serializers.data)
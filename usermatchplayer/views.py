from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserMatchPlayer
from .serializers import UserMatchPlayerSerializer
import json
# Create your views here.


class UserMatchPlayerView(APIView):
    """
    Method for handling GET and POST request on UserMatchPlayer model.
    """
    def get(self,request):
        usermatchplayer=UserMatchPlayer.objects.all()
        serializer=UserMatchPlayerSerializer(usermatchplayer,many=True)
        return Response(serializer.data)

    def post(self,request):
        data=request.data
        if 'data' in data:
            data=json.loads(data['data'])
        serializers=UserMatchPlayerSerializer(data=data,many=True)
        serializers.is_valid()
        serializers.save()
        return Response(serializers.data)
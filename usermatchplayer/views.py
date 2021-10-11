from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserMatchPlayer
from .serializers import UserMatchPlayerSerializer
# Create your views here.


class UserMatchPlayerView(APIView):
    
    def get(self,request):
        usermatchplayer=UserMatchPlayer.objects.all()
        serializer=UserMatchPlayerSerializer(usermatchplayer,many=True)
        return Response(serializer.data)

    def post(self,request):
        data=request.data
        serializers=UserMatchPlayerSerializer(data=data)
        serializers.is_valid()
        serializers.save()
        return Response(serializers.data)
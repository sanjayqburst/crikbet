from rest_framework.response import Response
from player.serializers import PlayerSerializer
from .models import Players
from rest_framework.views import APIView


# Create your views here.
class PlayerView(APIView):
    
    def get(self,request):
        player=Players.objects.all()
        serializers=PlayerSerializer(player, many=True)
        return Response(serializers.data)

    def post(self,request):
        data=request.data
        serializers=PlayerSerializer(data=data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data)
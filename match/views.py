from rest_framework.response import Response
from rest_framework.views import APIView
from match.serializers import MatchSerializer
from .models import Matches
# Create your views here.
class MatchView(APIView):
    """
    View for handling requests about match data.
    """

    def get(self,request):
        """
        Handleds get request for match view.
        """
        match=Matches.objects.all()
        serializer=MatchSerializer(match,many=True)
        return Response(serializer.data)

    def post(self,request):
        """
        Handleds post request for match view.
        """
        data=request.data
        serializers=MatchSerializer(data=data)
        serializers.is_valid()
        serializers.save()
        return Response(serializers.data)

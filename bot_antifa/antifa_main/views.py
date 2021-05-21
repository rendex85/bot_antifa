from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from antifa_main.models import User
from antifa_main.serializers import UserBaseSerializer
from bot_logic.main import main_loop


class UsersListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserBaseSerializer

@api_view(['POST'])
def BotTurner(request):
    """
    :request format:
    {
    "turn_bool": json.bool()
    }

    :returns:
    status loop
    """
    try:
        turn_bool = request.data.get('turn_bool')
        main_loop.TURN_ON = turn_bool
        return Response(f'now loop status: {turn_bool}')
    except:
        return Response(status=400)

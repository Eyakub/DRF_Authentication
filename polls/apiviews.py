from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets

from .models import Poll, Choice
from .serializers import PollSerializer, ChoiceSerializer, VoteSerializer, UserSerializer


"""
viewsets.ModelViewSet - when you are going to allow all or most of CRUD
operations on a model

generics.* - when you only want to allow some operations on a model

APIView when you want to completely customize the behaviour
"""

"""
ListCreateAPIView - get a list of entities or create them. 
Allow GET and POST
"""
class PollList(generics.ListCreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


"""
RetriveDestroyAPIView - retrive an individual entity details or delete the entity
Allows GET and DELETE
"""
class PollDetail(generics.RetrieveDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class ChoiceList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Choice.objects.filter(poll_id=self.kwargs['pk'])
        return queryset
    serializer_class = ChoiceSerializer



"""
CreateAPIView - Allows creating entities, but not listing them
Allows POST
"""
# class CreateVote(generics.CreateAPIView):
#     serializer_class = VoteSerializer


class CreateVote(APIView):
    serializer_class = VoteSerializer

    def post(self, request, pk, choice_pk):
        voted_by = request.data.get('voted_by')
        data = {'choice': choice_pk, 'poll': pk, 'voted_by': voted_by}
        serializer = VoteSerializer(data=data)
        if serializer.is_valid():
            vote = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""
Viewsets
"""
class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


"""
User
"""
class UserCreate(generics.CreateAPIView):
    serializer_class = UserSerializer
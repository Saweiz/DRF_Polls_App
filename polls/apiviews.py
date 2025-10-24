# API View
from rest_framework.views import APIView

# Get object from database
from django.shortcuts import get_object_or_404

# Generic Views
from rest_framework import generics

# Viewsets
from rest_framework import viewsets

# Models and Serializers
from .models import Poll, Choice, Vote
from django.contrib.auth.models import User
from .serializers import PollSerializer, ChoiceSerializer, VoteSerializer, UserSerializer

# Response and HTTP Status
from rest_framework import status
from rest_framework.response import Response

# Login API
from django.contrib.auth import authenticate

# Access control
from rest_framework.exceptions import PermissionDenied

# Generic Views
# class PollList(generics.ListCreateAPIView):
#     queryset = Poll.objects.all()
#     serializer_class = PollSerializer

# class PollDetail(generics.RetrieveDestroyAPIView):
#     queryset = Poll.objects.all()
#     serializer_class = PollSerializer

class ChoiceList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Choice.objects.filter(poll_id=self.kwargs["pk"])
        return queryset
    serializer_class = ChoiceSerializer

    def create(self, request, *args, **kwargs):
        poll = Poll.objects.get(pk=self.kwargs["pk"])
        if not request.user == poll.created_by:
            return PermissionDenied("You can not create choice for this poll.")
        else:
            return super().create(request, *args, **kwargs)


class ListVote(generics.ListAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

class UserListCreate(generics.ListCreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    def get_queryset(self):
        queryset = User.objects.all()
        return queryset
    serializer_class = UserSerializer



# Custom API View - POST method
class CreateVote(APIView):
    def post(self, request, pk, choice_pk):
        voted_by = request.data.get("voted_by")
        data = {"choice": choice_pk, "poll": pk, "voted_by": voted_by}
        serializer = VoteSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

class UserDetail(APIView):
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        data = UserSerializer(user).data
        return Response(data)

# Viewset Views
class PollViewset(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

    def destroy(self, request, *args, **kwargs):
        poll = Poll.objects.get(pk=self.kwargs["pk"])
        if not request.user == poll.created_by:
            return PermissionDenied("You are not allowed to delete this poll.")
        else:
            super().destroy(request, *args, **kwargs)


# Login API
class LoginView(APIView):
    permission_classes = ()

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        user_id = get_object_or_404(User, username=username)
        if user:
            return Response({'token': user.auth_token.key, 'id': user_id.id})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)
"""
# Using APIView

from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Poll
from .serializers import PollSerializer

class PollList(APIView):
    def get(self, request):
        polls = Poll.objects.all()[:20]
        data = PollSerializer(polls, many=True).data
        return Response(data)

class PollDetail(APIView):
    def get(self, request, pk):
        poll = get_object_or_404(Poll, pk=pk)
        data = PollSerializer(poll).data
        return Response(data)

"""
import messages
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Activity

from .serializers import ActivityViewSerializer, ActivityPostSerializer
from .serializers import AssistantSerializer, PotentialAttendeeSerializer
from .serializers import VoteSerializer

# Create your views here.
class ActivityList(APIView):
    def get(self, request, format=None):
        activities = Activity.objects.all()
        serializer = ActivityViewSerializer(activities, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ActivityPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            messages.send_message(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ActivityDetail(APIView):
    def get_object(self, pk):
        try:
            return Activity.objects.get(pk=pk)
        except Activity.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        activity = self.get_object(pk)
        serializer = ActivityViewSerializer(activity)
        return Response(serializer.data)

class VoteList(APIView):
    def post(self, request, format=None):
        serializer = VoteSerializer(data=request.data)
        if serializer.is_valid():
            activity = Activity.objects.get(pk=request.data['activity'])
            if request.data['type_vote'] == 0:
                activity.down_vote += 1
            else:
                activity.up_vote += 1
            activity.save()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PotentialAttendeeList(APIView):
    def post(self, request, format=None):
        serializer = PotentialAttendeeSerializer(data=request.data)
        if serializer.is_valid():
            activity = Activity.objects.get(pk=request.data['activity'])
            activity.count_potential_attendee += 1
            activity.save()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AssistantList(APIView):
    def post(self, request, format=None):
        serializer = AssistantSerializer(data=request.data)
        if serializer.is_valid():
            activity = Activity.objects.get(pk=request.data['activity'])
            activity.count_assistant += 1
            activity.save()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
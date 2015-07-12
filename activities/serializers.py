from rest_framework import serializers
from .models import Activity, Vote, PotentialAttendee, Assistant

class ActivityViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        depth = 1

class ActivityPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote

class PotentialAttendeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PotentialAttendee

class AssistantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assistant
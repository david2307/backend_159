from rest_framework import serializers
from .models import Community, Objective, SocialNetwork, Sector

class ObjectiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Objective

class CommunitySerializer(serializers.ModelSerializer):
    objectives = ObjectiveSerializer(many=True)

    class Meta:
        model = Community
        depth = 1

class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
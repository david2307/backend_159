import json
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Sector, Community, Objective, Member
from .models import CommunityRole
from persons.models import Person

from .serializers import CommunitySerializer, SectorSerializer
# Create your views here.

class CommunityList(APIView):
    def get(self, request, format=None):
        communities = Community.objects.all()
        serializer = CommunitySerializer(communities, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        name = request.data['name']
        purpose = request.data['purpose']
        sector = Sector.objects.get(pk=request.data['idSector'])

        community = Community(name=name, purpose=purpose, quantity=1, sector=sector)
        community.save()

        for objective in json.loads(request.data['objectives']):
            Objective(description=objective, community=community).save()

        person = Person.objects.get(pk=request.data['idPerson'])
        role = CommunityRole.objects.get(pk=1)

        member = Member(community=community, role=role, person=person)
        member.save()

        serializer = CommunitySerializer(community)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class SectorList(APIView):
    def get(self, request, format=None):
        sectors = Sector.objects.all()
        serializer = SectorSerializer(sectors, many=True)
        return Response(serializer.data)
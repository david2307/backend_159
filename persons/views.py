from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Person
from .serializers import PersonSerializer

# Create your views here.
class PersonList(APIView):

    def post(self, request, format=None):
        print request.data
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegisterGcm(APIView):
    def put(self, request, pk, format=None):
        print request.data
        person = Person.objects.get(pk=pk)
        person.id_device = request.data['idDevice']
        person.save()

        return Response(dict(idDevice=person.id_device, status=status.HTTP_202_ACCEPTED))

class Login(APIView):
    def get(self, request, format=None):
        email = request.GET['user']
        password = request.GET['password']

        person = Person.objects.filter(email=email, password=password).first()

        data = dict()

        if person:
            data['id'] = person.pk
            data['message'] = 'Login Exitoso'
        else:
            data['error'] = 1
            data['message'] = 'Credenciales Invalidas'

        return Response(data)
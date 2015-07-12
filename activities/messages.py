import json
from gcm import *
from persons.models import Person

API_KEY = 'AIzaSyDczNjPCpfyYH8ZmAHxljA7NmvuoUp6jog'

def send_message(message):
    print message
    persons = Person.objects.all()
    devices = list()
    for person in persons:
        devices.append(person.id_device)
    print devices
    gcm = GCM(API_KEY)
    gcm.json_request(registration_ids=devices, data=message)

def send_messages(devices, message):
    gcm = GCM(API_KEY)
    gcm.json_request(registration_ids=devices, data=message)
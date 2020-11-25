from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import RegistrationSerializer

@api_view(['POST',])
def registration_view(request):
    if request.method == "POST":
        ser = RegistrationSerializer(data=request.data)
        data = {}
        if ser.is_valid():
            users = ser.save()
            data['response']="Successfully Registred"
            data['email']=users.email
            data['username']=users.username
        else:
            data = ser.errors
        return Response(data)
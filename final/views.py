from django.shortcuts import redirect, render,get_object_or_404
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from .models import User
from .serializers import UserSerializer
from .models import User


def home(request):
    username = request.user.username
    return render(request,"home.html",locals())


@api_view(['POST',])
def Record(request):
    # get method handler
    if request.method == "POST":
        ser = UserSerializer(data=request.data)
        data = {}
        if ser.is_valid():
            users = ser.save()
            # obj = User()
            # obj.username = users.username
            # obj.name = users.name
            # obj.email = users.email
            # obj.save()
            data['response'] = "Successfully Registred"
            data['email'] = users.email
            data['username'] = users.username
        else:
            data = ser.errors
        return Response(data)
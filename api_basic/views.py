from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .models import Article
from .serializers import ArticleSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView

from rest_framework import generics
from rest_framework import mixins

from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework import viewsets
from django.shortcuts import get_object_or_404


# Create your views here.

#Viewsets
# class articleViewSet(viewsets.ViewSet):
#class articleViewSet(viewsets.ModelViewset):
#Two Lines
class articleViewSet(viewsets.GenericViewSet,mixins.ListModelMixin, mixins.CreateModelMixin,
                     mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
    serializer_class = ArticleSerializer  # Serializing or deserializing the input.
    queryset = Article.objects.all()  # getting all datas from model




    #No get,post,update options list,create,retrieve,destroy

    # def list(self,request):
    #     article = Article.objects.all()
    #     ser = ArticleSerializer(article,many=True)
    #     return Response(ser.data)
    #
    # def create(self,request):
    #     article = ArticleSerializer(data=request.data)
    #     if article.is_valid():
    #         article.save()
    #         return Response(article.data,status=status.HTTP_201_CREATED)
    #     return Response(article.errors,status=status.HTTP_400_BAD_REQUEST)
    #
    # def retrieve(self,request,pk=None):
    #     queryset = Article.objects.all()
    #     article = get_object_or_404(queryset,pk=pk)
    #     ser = ArticleSerializer(article)
    #     return Response(ser.data)
    #
    # def update(self,request,pk=None):
    #     queryset = Article.objects.all()
    #     article = get_object_or_404(queryset,pk=pk)
    #     ser = ArticleSerializer(article,data=request.data)
    #     if ser.is_valid():
    #         ser.save()
    #         return Response(ser.data)
    #     return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
    #
    # def destroy(self,request,pk=None):
    #     queryset = Article.objects.all()
    #     article = get_object_or_404(queryset,pk=pk)
    #     article.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)




















# GenericApiView based views,Specially for avoiding reusability of Code
# Mixins helps to provide actions like get,post etc.
# GenericAPiView combinig one or two more mixins
class genericAPiView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                     mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
    serializer_class = ArticleSerializer  # Serializing or deserializing the input.
    queryset = Article.objects.all()  # getting all datas from model

    lookup_field = 'id'

    # Authentication classes for session auth,Basic auth
    # authentication_classes = [SessionAuthentication,BasicAuthentication]
    # TokenAuthentication
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # ListModelMixin and RetrieveModelMixin
    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        return self.list(request)

    # CreateModelMixin
    def post(self, request):
        return self.create(request)

    # UpdateModelMixin
    def put(self, request, id):
        return self.update(request, id)

    # DestroyModelMixin
    def delete(self, request, id):
        return self.destroy(request, id)


# Class based API Views
class articleApiView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        ser = ArticleSerializer(articles, many=True)
        return Response(ser.data)

    def post(self, request):
        ser = ArticleSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


class article_detail_api(APIView):
    def get_object(self, id):
        try:
            return Article.objects.get(pk=id)
        except Article.DoesNotExist:
            raise Http404

    def get(self, request, id):
        article = self.get_object(id)
        ser = ArticleSerializer(article)
        return Response(ser.data)

    def put(self, request, id):
        article = self.get_object(id)
        ser = ArticleSerializer(article, data=request.data)
        if ser.is_valid():
            return Response(ser.data)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        article = self.get_object(id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Function based Api Views
# @csrf_exempt
# JSONResponse to Response
# status number to status.HTTP
# More Concise

@api_view(['GET', 'POST'])
def article_list(request):
    # list all objects GET
    if request.method == "GET":
        articles = Article.objects.all()
        ser = ArticleSerializer(articles, many=True)
        # return JsonResponse(ser.data,safe=False)
        return Response(ser.data)

    # Create new object POST
    elif request.method == "POST":
        # data = JSONParser().parse(request) #dict
        # ser = ArticleSerializer(data=data) #serializer
        # request.data similar to request.post convert to arbitary form(auto Parsing)

        ser = ArticleSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


# @csrf_exempt
@api_view(["GET", "PUT", "DELETE"])
def article_detail(request, pk):
    # Getting Article
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        ser = ArticleSerializer(article)
        return Response(ser.data)

    elif request.method == "PUT":
        # data = JSONParser().parse(request)
        ser = ArticleSerializer(article, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

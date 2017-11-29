from Cheese.utils.mongo_connection import MongoConnection
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Algorithm
from .serializers import AlgorithmSerializer


class AlgorithmList(APIView):
    
    def get(self,request):
        algorithm = Algorithm.objects.all()
        serializer = AlgorithmSerializer(algorithm, many = True)
        return Response(serializer.data)
        
    
    def post(self):
        pass



def index(request):
    conn = MongoConnection()
    carterrain = conn.db['carterrains']
    cursor = carterrain.find({})
    
    return HttpResponse("<h1> Welcome to Cheesepy</h1>")


def algorithm(request, algorithm_code,dataset):
   return HttpResponse("<h2>You Chose Algorithm Id : " + str(dataset) + str(algorithm_code) + "</h2>")


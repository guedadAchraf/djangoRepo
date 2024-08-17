from django.shortcuts import render

# Create your views here.


def home(request) :
    return render(request,'home.html')


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class HelloAchrafView(APIView):
    def get(self, request):
        return Response({'message': 'Hello, Achraf'}, status=status.HTTP_200_OK)

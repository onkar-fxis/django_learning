from django.shortcuts import render
from django.http import HttpResponse

from .models import Transactions
from .serializers import TransactionSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.views import APIView

# Create your views here.
# import HttpRsponse

# request => response 

def say_hello(request):
    # pull data from db
    # tranform data
    # send email
    # return HttpResponse("hello world")
    return render(request , 'hello.html' ,{'name':'onkar'})

# @api_view()
# def get_transactions(request):
#     queryset = Transactions.objects.all()
#     serializer = TransactionSerializer(queryset , many = True)
#     return Response({
#         "data" : serializer.data
#     })

class TransactionAPI(APIView):

    def get(self, request):
        queryset = Transactions.objects.all()
        serilizer = TransactionSerializer(queryset , many = True)
        return Response({
            "message" : "This is get request",
            "data" : serilizer.data
        })
    
    def post(self , request):
        data =request.data 
        serilizer = TransactionSerializer(data = data)
        if not serilizer.is_valid():
            return Response({
                "message": "error",
                "errors" : serilizer.errors
            })
        serilizer.save()
        return Response({
            "message": "Post request succsfull"
        })
    
    def put(self, request) :
        return Response({
            "message": "This is a Put requst"
        })
    
    def delete(self, request):
        return Response({
            "message": "This is a delete request"
        })

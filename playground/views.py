from django.shortcuts import render
from django.http import HttpResponse

from .models import Transactions
from .serializers import TransactionSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
# import HttpRsponse

# request => response 

def say_hello(request):
    # pull data from db
    # tranform data
    # send email
    # return HttpResponse("hello world")
    return render(request , 'hello.html' ,{'name':'onkar'})

@api_view()
def get_transactions(request):
    queryset = Transactions.objects.all()
    serializer = TransactionSerializer(queryset , many = True)
    return Response({
        "data" : serializer.data
    })


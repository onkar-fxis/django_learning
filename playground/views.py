from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# import HttpRsponse

# request => response 

def say_hello(request):
    # pull data from db
    # tranform data
    # send email
    # return HttpResponse("hello world")
    return render(request , 'hello.html' ,{'name':'onkar'})


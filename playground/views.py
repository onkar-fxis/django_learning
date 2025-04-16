
from django.shortcuts import render
from django.http import HttpResponse
from .models import Transactions
from .serializers import TransactionSerializer, RegisterSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated



def say_hello(request):
    return render(request, 'hello.html', {'name': 'onkar'})


class TransactionAPI(APIView):
    def get(self, request):
        queryset = Transactions.objects.all()
        serializer = TransactionSerializer(queryset, many=True)
        return Response({
            "message": "All transactions",
            "data": serializer.data
        })

    def post(self, request):
        data = request.data
        serializer = TransactionSerializer(data=data)
        if not serializer.is_valid():
            return Response({
                "message": "error",
                "errors": serializer.errors
            })
        serializer.save()
        return Response({
            "message": "Post request successful",
            "data": serializer.data
        })

    def put(self, request):
        data = request.data
        if not data.get("id"):
            return Response({
                "message": "error",
                "errors": "id is required"
            })

        transaction_data = Transactions.objects.get(id=data.get("id"))
        serializer = TransactionSerializer(transaction_data, data=data, partial=True)

        if not serializer.is_valid():
            return Response({
                "message": "data not saved",
                "errors": serializer.errors
            })
        serializer.save()
        return Response({
            "message": "This is a PUT request",
            "data": serializer.data
        })

    def delete(self, request):
        data = request.data
        if not data.get("id"):
            return Response({
                "message": "error",
                "errors": "id is required field"
            })
        Transactions.objects.get(id=data.get("id")).delete()
        return Response({
            "message": "data deleted",
            "data": {}
        })


class RegisterView(APIView):
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "message": "User created successfully",
                "status": True,
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        data = request.data
        username = data.get('username')
        password = data.get('password')
        user = User.objects.filter(username=username).first()
        if user and user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return Response({
                "access_token": str(refresh.access_token),
                "refresh_token": str(refresh)
            })
        return Response({
            "message": "Invalid credentials"
        }, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(APIView):
    permission_classes = [IsAuthenticated] 
    def get(self, request):
        user = request.user
        serializer = RegisterSerializer(user)
        return Response(serializer.data)











# notes
# from django.shortcuts import render
# from django.http import HttpResponse

# from .models import Transactions
# from .serializers import TransactionSerializer , RegisterSerializer
# from rest_framework.response import Response
# from rest_framework.decorators import api_view

# from rest_framework.views import APIView
# from rest_framework import status

# from rest_framework_simplejwt.tokens import RefreshToken
# from django.contrib.auth.models import User



# # Create your views here.
# # import HttpRsponse

# # request => response 

# def say_hello(request):
#     # pull data from db
#     # tranform data
#     # send email
#     # return HttpResponse("hello world")
#     return render(request , 'hello.html' ,{'name':'onkar'})

# # @api_view()
# # def get_transactions(request):
# #     queryset = Transactions.objects.all()
# #     serializer = TransactionSerializer(queryset , many = True)
# #     return Response({
# #         "data" : serializer.data
# #     })

# class TransactionAPI(APIView):

#     def get(self, request):
#         queryset = Transactions.objects.all()

    

#         serilizer = TransactionSerializer(queryset , many = True)

#         return Response({
#             "message": "All transactions",
           
#             "data": serilizer.data
#         })
    
#     def post(self , request):
#         data =request.data 
#         serilizer = TransactionSerializer(data = data)
#         if not serilizer.is_valid():
#             return Response({
#                 "message": "error",
#                 "errors" : serilizer.errors
#             })
#         serilizer.save()
#         return Response({
#             "message": "Post request succsfull",
#             "data": serilizer.data
#         })
    
#     def put(self, request) :

#         data = request.data 

#         if not data.get("id"):
#             return Response({
#                 "message": "error",
#                 "errors" : "id is required"
#             })
        
#         transactiondata = Transactions.objects.get(id = data.get("id"))
#         serializer = TransactionSerializer(transactiondata, data = data ,  partial = True)

#         if not serializer.is_valid():
#             return Response({
#                 "message":"data not saved",
#                 "errors" : serializer.errors
#             })
#         serializer.save()
#         return Response({
#             "message": "This is a Put requst",
#             "data" : serializer.data
#         })
    
#     def delete(self, request):

#         data =  request.data 

#         if not data.get("id"):
#             return Response({
#                 "message" : "error",
#                 "errors" : "id is required field"
#             })
#         transaction = Transactions.objects.get(id = data.get("id")).delete()

#         return Response({
#             "message": "data deleted",
#             "data" : {}
#         })




# class RegisterView(APIView):
#     def post(self, request):
#         data = request.data 
#         serializer = RegisterSerializer(data = data)   
#         if serializer.is_valid():
#             user = serializer.save()
#             return Response({
#                 "message" : "User created successfully",
#                 "status" : True,
#                 "data" : serializer.data
#             }, status= status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


#     class LoginView(APIView):
#         def post(self, request):
#             data = request.data 
#             username = data.get('username')
#             password = data.get('password')
#             user = User.objects.filter(username = username).first()
#             if user and user.check_password(password):
#                 refresh = RefreshToken.for_user(user)
#                 return Response({
#                     "access_token": str(refresh.access_token),
#                     "refresh_token" : str(refresh)
#                 })
#             return Response({
#                 "message" : "invalid credential"
#             },status= status.HTTP_400_BAD_REQUEST)


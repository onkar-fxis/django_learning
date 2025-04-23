from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import StudentModel
from .serializer import StudentSerializer

class AppView(APIView):

    def get_object(self, id):
        try:
            return StudentModel.objects.get(id=id)
        except StudentModel.DoesNotExist:
            raise Http404

    def get(self, request, id=None):
        if id is not None:
            student = self.get_object(id)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        else:
            students = StudentModel.objects.all()
            serializer = StudentSerializer(students, many=True)
            return Response(serializer.data)

    def post(self, request, id=None):
        if id is not None:
            return Response({"error": "POST not allowed on detail endpoint"}, status=405)

        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def put(self, request, id=None):
        if id is None:
            return Response({"error": "PUT requires student ID"}, status=400)

        student = self.get_object(id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def patch(self, request, id=None):
        if id is None:
            return Response({"error": "PATCH requires student ID"}, status=400)

        student = self.get_object(id)
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id=None):
        if id is None:
            return Response({"error": "DELETE requires student ID"}, status=400)

        student = self.get_object(id)
        student.delete()
        return Response(status=204)

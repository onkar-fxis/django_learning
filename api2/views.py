from django.shortcuts import render
from django.http import JsonResponse
from .models import StudentModel
from .serializer import StudentSerializer

# Create your views here.

# def student_details(request):
#     stu = StudentModel.objects.all()
#     serializer = StudentSerializer(stu , many = True)
#     return JsonResponse(serializer.data, safe=False)


def student_details(request):
    try:
        stu = StudentModel.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return JsonResponse(serializer.data, safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


def student_detail_by_id(request, id):
    try:
        stu = StudentModel.objects.get(id=id)
        serializer = StudentSerializer(stu)
        return JsonResponse(serializer.data, safe=False)
    except StudentModel.DoesNotExist:
        return JsonResponse({"error": "Student not found"}, status=404)



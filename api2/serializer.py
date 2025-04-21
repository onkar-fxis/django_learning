from rest_framework import serializers
from rest_framework import serializers
from .models import StudentModel

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = '__all__' 
        # excludes = []



# class StudentSerializer(serializers.Serializer):
#     name  = serializers.CharField( max_length=50)
#     roll = serializers.IntegerField()
#     city = serializers.CharField()
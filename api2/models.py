# from django.db import models

# # Create your models here.


# class StudentModel(models.Model):
#     name  = models.CharField( max_length=50)
#     roll = models.IntegerField()
#     city = models.CharField()



from django.db import models
from django.utils import timezone

class StudentModel(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)
    
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} (Roll: {self.roll})"

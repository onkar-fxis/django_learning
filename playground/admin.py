

# Register your models here.




from django.contrib import admin
from .models import Transactions
from api2.models import StudentModel

models = [Transactions, StudentModel]
for model in models:
    admin.site.register(model)

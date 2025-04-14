from django.urls import path
from playground import views


urlpatterns = [
        path("get-transaction/" , views.get_transactions)

]

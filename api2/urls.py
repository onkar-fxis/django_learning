from django.urls import path
from . import views

# URLconfig

urlpatterns = [
    path("", views.student_details),
    path("<int:id>/", views.student_detail_by_id),
]
  
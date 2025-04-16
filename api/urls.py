from django.urls import path
from playground import views
from playground.views import RegisterView, LoginView,ProfileView,LogoutView

urlpatterns = [
    path("transactions/" , views.TransactionAPI.as_view()),
    path('register/' , RegisterView.as_view()),
    path('login/', LoginView.as_view()),      
    path('profile/', ProfileView.as_view()),      
    path('logout/', LogoutView.as_view(), name='logout'),

]

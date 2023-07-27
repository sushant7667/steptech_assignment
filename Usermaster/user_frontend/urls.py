from django.urls import path,include
from django.contrib import admin
from user_frontend import views

urlpatterns = [
    path('hello_world', views.hello_world,name="hello_world"),
    path('Adduser_front', views.Adduser_front,name="Adduser_front"),
    path('Getuser_Front', views.Getuser_Front,name="Getuser_Front"),
    path('Updateuser_front/<int:id>', views.Updateuser_front,name="Updateuser_front"),
    path('Deleteuser_front/<int:id>', views.Deleteuser_front,name="Deleteuser_front"),
]

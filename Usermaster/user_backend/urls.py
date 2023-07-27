from django.urls import path
# from .views import weather_forecast, get_weather_forecast, receive_weather_forecast
from user_backend import views
urlpatterns = [
    # Other URL patterns
    path('AddUser', views.AddUser,name="AddUser"),
    # path('home', views.home,name="home"),
    path('GetUser', views.GetUser,name="GetUser"),
    path('GetUserId/<int:id>', views.GetUserId,name="GetUserId"),
    path('UpdateUser/<int:id>', views.UpdateUser,name="UpdateUser"),
    path('deleteuser/<int:id>', views.deleteuser,name="deleteuser")
]
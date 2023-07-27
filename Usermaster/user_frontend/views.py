from django.shortcuts import render,redirect
from . import views
from rest_framework.decorators import api_view
from .models import *
import requests
from rest_framework.response import Response
from django.contrib import messages
from user_backend.models import User
from django.http import HttpResponse

# Create your views here.
hellourl='http://127.0.0.1:8000/user_backend/hello'
addurl='http://127.0.0.1:8000/user_backend/AddUser'
geturl='http://127.0.0.1:8000/user_backend/GetUser'
getidurl='http://127.0.0.1:8000/user_backend/GetUserId/'
updateurl='http://127.0.0.1:8000/user_backend/UpdateUser/'
deleteurl='http://127.0.0.1:8000/user_backend/deleteuser/'

def hello_world(request):
        response = requests.get(hellourl)
        geodata = response.json()
        return HttpResponse(geodata['message'])

def Adduser_front(request):
    if request.method == 'POST':
        data={}
        data['name'] = request.POST.get('name')  
        data['email'] = request.POST.get('email')
        data['role'] = request.POST.get('role')
        print("data",data)
        responseurl=requests.post(addurl,data=data)
        print("responseurl",responseurl)
        result = responseurl.json()
        print("result",result)

        if result['response']['n'] == 1:
                messages.success(request, result['response']['msg'])
                return redirect('user_frontend:Getuser_Front')
        else:
                messages.error(request, result['response']['msg'])
                return redirect('user_frontend:Getuser_Front') 
    else:
        return render(request,'add.html')

def Getuser_Front(request):
        response = requests.get(geturl)
        geodata = response.json()
        print("geodata",geodata)
        return render(request,'view.html',{'data':geodata['data']}) 

def Updateuser_front(request,id):
        if request.method == "GET":
                getUser = getidurl + str(id)
                response = requests.get(getUser)
                geodata = response.json()
                return render(request,'update.html',{'data':geodata['data']})
        else:
                data={}
                data['name'] = request.POST.get('name')  
                data['email'] = request.POST.get('email')
                data['role'] = request.POST.get('role')
                updateUser = updateurl + str(id)
                responseUrl = requests.post(updateUser,data=data)
                result = responseUrl.json()
                print("result",result)
                if result['response']['n'] == 1:
                        messages.success(request, result['response']['msg'])
                        return redirect('user_frontend:Getuser_Front')
                else:
                        messages.error(request, result['response']['msg'])
                        return redirect('user_frontend:Getuser_Front')

def Deleteuser_front(request,id):
        deleteuser=deleteurl + str(id)
        responseUrl = requests.get(deleteuser)
        result = responseUrl.json()
        print ("result",result)
        if result['response']['n'] == 1:
                messages.success(request, result['response']['msg'])
                return redirect('user_frontend:Getuser_Front')
        else:
                messages.error(request, result['response']['msg'])
                return redirect('user_frontend:Getuser_Front')
            



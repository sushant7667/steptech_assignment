from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import views
from rest_framework.decorators import api_view
from .models import *
from .serializer import *
import requests
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def hello(request):
    return Response({"message": "Hello, World!"})
    
@api_view(['POST'])
def AddUser(request):
    data={}
    data['name'] = request.POST.get('name')  
    data['email'] = request.POST.get('email')
    data['role'] = request.POST.get('role')

    print("data",data)
    # email validation
    emailvalidation=User.objects.filter(isactive=True,email=request.POST.get('email')).first()
    print("emailvalidation",emailvalidation)  
    if emailvalidation is not None:
        Response_ = {
            "data":{},
            "response":{
                "n":0,
                "msg":"User with this Email id already exists",
                "Status":"Failed"

            }
        }
        return Response(Response_)
    serializer=userserializer(data=data)

    if serializer.is_valid():
        serializer.save()
        Response_ = {
            "data":serializer.data,
            "response":{
                "n":1,
                "msg":"User save succesfully",
                "Status":"Success"

            }
        }
        return Response(Response_)
    else:
        Response_ = {
            "response":{
                "data":serializer.errors,
                "n":0,
                "msg":"Failed to save data",
                "Status":"Failed"

            }
        }
        return Response(Response_)

@api_view(['GET'])
def GetUser(request):
    user = User.objects.filter(isactive=True).order_by('id')
    serializer = userserializer(user, many=True)

    if serializer.data:
        response_data = {
            "data": serializer.data,
            "response": {
                "n": 1,
                "msg": "Data found successfully",
                "Status": "Success"
            }
        }
        return Response(response_data)
    else:
        response_data = {
            "data": {},
            "response": {
                "n": 0,
                "msg": "No data found",
                "Status": "Failed"
            }
        }
        return Response(response_data)

@api_view(['GET'])
def GetUserId(request,id):
    getUser=User.objects.filter(id=id,isactive=True).first()
    if getUser is not None:
        serializer=userserializer(getUser)
        Response_ = {
            "data":serializer.data,
            "response":{
                "n":1,
                "msg":"User Data has been saved successfully",
                "Status":"Success"

            }
        }
        return Response(Response_)
    else:
        Response_ = {
            "data":{},
            "response":{
                "n":0,
                "msg":"No user found",
                "Status":"Failed"

            }
        }
        return Response(Response_)

@api_view(['POST'])
def UpdateUser(request,id):
    getUserObject=User.objects.filter(id=id,isactive=True).first()
    print("getUserObject",getUserObject)
    if getUserObject is not None:
        data={}
        data['name'] = request.POST.get('name')  
        data['email'] = request.POST.get('email')
        data['role'] = request.POST.get('role')
        print("dataaaa",data)
        emailvalidation=User.objects.filter(isactive=True,email=request.POST.get('email')).exclude(id=id).first() 
        print("emailvalidation",emailvalidation)          
        if getUserObject.email==data ['email']and emailvalidation is not None:
            Response_ = {
                "data":{},
                "response":{
                    "n":0,
                    "msg":"User with this Email id already exists",
                    "Status":"Failed"

                }
            }
            return Response(Response_)
        serializer=userserializer(getUserObject,data=data)
        # print("serializer",serializer.data)
        if serializer.is_valid():
            serializer.save()
            print("save",serializer.data)
            Response_ = {
                "data":serializer.data,
                "response":{
                    "n":1,
                    "msg":"User Data has been Updated successfully",
                    "Status":"Success"

                }
            }
            return Response(Response_)
        else:
            print("err",serializer.errors)
            Response_ = {
                "data":serializer.errors,
                "response":{
                    "n":0,
                    "msg":"Error updating User",
                    "Status":"Success"

                }
            }
            return Response(Response_)
    else:
        Response_ = {
            "data":{},
            "response":{
                "n":0,
                "msg":"User not Found",
                "Status":"Failed"

            }
        }
        return Response(Response_)

@api_view(['GET'])
def deleteuser (request,id):
    getUserObject=User.objects.filter(id=id,isactive=True).first()
    if getUserObject is not None:
        data={}
        data['isactive']=False
        serializer=userserializer(getUserObject,data=data)
        if serializer.is_valid():
            serializer.save()
            Response_ = {
                "data":serializer.data,
                "response":{
                    "n":1,
                    "msg":"user deleted successfully",
                    "Status":"Success"
                }
            }
            return Response(Response_)
        else:
            Response_ = {
                "data":serializer.errors,
                "response":{
                    "n":0,
                    "msg":"Error Deleting user",
                    "Status":"Failed"
                }
            }
            return Response(Response_)
    else:
        Response_ = {
            "data":{},
            "response":{
                "n":0,
                "msg":"No data found",
                "Status":"Failed"

            }
        }
        return Response(Response_)

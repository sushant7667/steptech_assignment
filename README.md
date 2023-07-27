# steptech_assignment
steptech_assignment
1) I used Django restframework to perform this task and use postman connect to the databse.I use postgresql as a DB.
   In this project I used serializer method.
2) I have perform user can add ,update and delete operation.
3) Firstly I create virtual environment as env then I used this cmd for create the project: django-admin startproject Usermaster
4) In usermaster setting I have mention this both apps name in install app and give the template ands static file path.
5) Also i have mention in settings.py databse ENGINE, user and password to coonect the database pgadmin
6) In usermaster i have created app user_backend and user_frontend
    I)user_backend:py manage.py startapp user_backend 
    II)user_frontend:py manage.py startapp user_frontend  
7) In user backend add models.py,serializers.py urls.py and views.py also I applied email validation for the user using python
8) In frontend i userd postman api to get json response and msgs also
9) created the template folder to save html pages and in static folder to save css files.
   

### Project Folder
---
First We have to create a new folder, in our example i created the following folder.<br>
Du_CAAS_Upload_Attendence

> mkdir Du_CAAS_Upload_Attendence 

<br>

> cd Du_CAAS_Upload_Attendence

<br>

### Virtual Environment for the project
---
create a new virtual environment in the folder with, then activate it
> python3 -m venv caasEnv

<br>

> source caasEnv/bin/activate 

### Install Django inside the project folder
--- 
Notice:Note that when the virtualenv is activated, python and pip are added to PATH from the virtualenv, so you don't need to worry about using python3 or pip3. And all your packages will be installed under ./venv, well isolated from everything else in your system.
<br>
That is why we can use pip install django no need for pip3

>pip install django

<br>

### Django New project and new Application
---
Create a new Djanog project, and then create a new Application we are goint to calle it "addatt" short for add attendence
> django-admin DUAtt
<br>

> python manage.py startup addatt

This will add a primary app, but we must create other applicaitons, the django project is a list of connected applicaitons. But keep in maind the primary app is the main app from which we can call other applicaitons.
<br>
The primary app will take the name the of the project folder. for example in our case it will be "DUAtt"


### Creating a URL and a View for the Web Application
---
Inside the primary app, which is ‘DUAtt,’ make the following configurations. Open ‘urls.py’ and add the pattern to point to the ‘tutorial’ app. Import ‘include’ and add the path to the ‘urls.py’ file inside ‘addatt’

> Path(‘’,include(‘addatt.urls’))>
 
<br>

### Homepage for addatt app
--- 
Go to ‘addatt.urls.py’ and import ‘views’ Add the app name for future reference and add the path to point to a homepage view for the tutorial app

>Path(‘’,views.homepage, name=“homepage”)

<br>

### Homepage View for
--- 
But so far we don’t have any view called homepage. So, add a simple HttpResponse view called homepage. Don’t forget to import HttpResponse from django.http as shown below:
> def homepage(request):<br>
> &emsp;return HttpResponse("First App")

<br>

### Start your App
--- 
Now, boot up the web server and run the following command
> python manage.py runserver
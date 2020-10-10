# Setting Up a Django Project

<div style="background-color:#f1f1f1;padding:0 0 0 10px;color:#333;font-weigh:bold;">

## Part one

</div>
Here we are going to do three important steps:<br>
1. Create a project folder in your<br>
2. Create a virtual environment for our project <br>
3. Install Django
   
<br>
<br>
<br>

### Project Folder

First We have to create a new folder, in our example i created the following folder.<br>
Du_CAAS_Upload_Attendence

> mkdir Du_CAAS_Upload_Attendence 

<br>

> cd Du_CAAS_Upload_Attendence

<br>

### Create a Virtual Environment for the Project
---
create a new virtual environment in the folder with, then activate it
> python3 -m venv caasEnv

<pre>
-m means module, and the name of the module to be opened is venv<br>
the code "python -m venv caasEnv", means python open the module named venv and create a new virtual environment called caasEnv
</pre>
<br>

> source caasEnv/bin/activate 

you can also use this code directly to get the virtual environment automatically activated, and install the application's dependencies.

>python -m pip install -r requirements.txt

### Install Django inside the project folder
--- 
Notice:Note that when the virtualenv is activated, python and pip are added to PATH from the virtualenv, so you don't need to worry about using python3 or pip3. And all your packages will be installed under ./venv, well isolated from everything else in your system.
<br>
That is why we can use pip install django no need for pip3

>pip install django

you can also use this code , to install any package 
>python3 -m pip install django
<br>

you can verify django installation by:
>django-admin --version 
<br>
<br>
---- 
<br>

<div style="background-color:#f1f1f1;padding:0 0 0 10px;color:#333;font-weigh:bold;">

## Part Two

</div>

Here we are going to do two important steps:<br>
1. Creating the primary application database "DUAtt"
2. Creating a new application "addatt".
3. Adding the new created project to settings.py
4. creating the addatt urls.py and configuring the URLs to the application
5. Creating the view functions inside the addatt

<br>

### Django New project and new Application
---
Create a new Django project "DUAtt", after that create a new Application. We are going to calle it "addatt" short for add attendence
> django-admin startproject DUAtt
<br>

To create the new application, you have to open the folder DUAtt, which newly created, then from inside that folder you have to issue the following command:

> python manage.py startapp addatt

This will add a primary app, but we must create other application, the django project is a list of connected application. But keep in maind the primary app is the main app from which we can call other application
<br>
The primary app will take the name the of the project folder. for example in our case it will be "DUAtt"

after creating the new app it is important to go to the settings.py file and add the new app "addatt" into the "INSTALLED_APPS" section

<br><br>
![](images/installed_apps.png)

---

### Creating a URL and a View for the Web Application
---
Inside the primary app, which is ‘DUAtt,’ make the following configurations. Open ‘urls.py’ and add the pattern to point to the ‘tutorial’ app. Import ‘include’ and add the path to the ‘urls.py’ file inside ‘addatt’.

> path(‘’,include(‘addatt.urls’)),<br>
> path('addatt/' include('addatt.urls)),

here if the user type the web address without andy extra details, it will open the addatt app, and also if he typed addatt as extra details in the website it also will open the addatt app

<br>
Notice: you may need to add "include" library <br>

---

 
 ![](images/primary_app_url.png)
this code means when the site start go to the application named "addatt" and open urls file and check for lins there. The file urls.py, not yet created and you have to create it manually.


<br>


<br>

### Homepage for addatt app
--- 
Go to ‘addatt.urls.py’ and import ‘views’ Add the app name for future reference and add the path to point to a homepage view for the tutorial app

>Path(‘’,views.homepage, name=“homepage”)

<br>
See the image bellow a new file urls.py created and inside it the above code added
we have to add application namespace " app_name='addatt', this is the namespace, which we use to identify this app especially when we using hyperlinks
--- 
![](images/addatt_url.png)

<br>

### Homepage View for
--- 
But so far we don’t have any view called homepage. So, add a simple HttpResponse view called homepage. Don’t forget to import HttpResponse from django.http as shown below:
> def homepage(request):<br>
> &emsp;return HttpResponse("First App")

<br>
here we imported "from django.http import HttpResponse" library

---
![](images/img3.png)


### Start your App
--- 
Now, boot up the web server and run the following command
> python manage.py runserver

---
<div style="background-color:#f1f1f1;padding:0 0 0 10px;color:#333;font-weigh:bold;">

## Part Three

</div>

Here we are going to create the templates in our projects<br>
1. create a new folder and call it template folder.
2. configure settings.py files for template folder.
3. Create a view that renders the request and maps to a template inside the template directory.
4. Configuring the STATIC file section in the settings.py file

---
Inside your project folder create a new folder and call it template.<br>
Django template is a way to dynamically generate HTML, XML, and PDF files in Django web framework. Django template contains the static parts of a desired HTML output and some special syntax that describes how dynamic content will be inserted.

<br>
This image shows the project structure after adding the folder templates

![](images/pro_str1.png)

<br>

All HTML files required in a project are stored inside a folder called template. But in order to tell Django to look for templates inside the directory, we have to perform some configuration.

<br>

Create an HTML page for our addatt home inside the template directory. Let us name it ‘home.html’

<br>

![](images/pro_str2.png)
<br>

Go to settings.py and make the following template configurations. Here, we are defining the directory path where Django should look for the template source files

> [os.path.join(BASE_DIR,'template')]

please checkout the images bellow<br>

![](images/settings.png)

<br>
please add the template configuration 
<br>

![](images/settings2.png)

<br>
<br>

### Create a view that renders the request and maps to a template inside the template directory

---



<br>
This view or view function is created inside the ‘addatt’ application, in the views.py file. Here, this view function is taking the request for the home page, and then renders a template called ‘home.html’, which is inside the template folder.
<br>

![](images/view_home.png)


<br>
<br>

Static files

Open the settings.py file and add the following code to the end of the file:<br>

`# Static files (CSS, JavaScript, Images)`<br>

> STATIC_URL = '/static/'

`# default static files settings for PythonAnywhere.`<br>
`# see https://help.pythonanywhere.com/pages/DjangoStaticFiles for more info`<br>
>MEDIA_ROOT = os.path.join(BASE_DIR, 'media')<br>
>MEDIA_URL = '/media/'<br>
>STATIC_ROOT = os.path.join(BASE_DIR, 'static')<br>
>STATIC_URL = '/static/'<br>

<br>
<br>
<br>

<div style="background-color:#f1f1f1;padding:0 0 0 10px;color:#333;font-weigh:bold;">

## Part Four

</div>

Here in this section we are going to make the following changes to our project:<br>
1. Configure the urls.py file in the primary application to display static files.
2. Create the upload.html.
3. Create a new view function inside the views.py to display the upload.html.
4. Configure the urls.py file to display the upload.html.
<br>
<br>
### The Basics of File Upload With Django

When files are submitted to the server, the file data ends up placed in **request.FILES.** <br>
The request.FILES is a dictionary-like object. Each key in request.FILES is the name from the `<input type="file" name="" />`. <br>
Each value in request.FILES is an UploadedFile instance.<br>

It is mandatory for the HTML form to have the attribute enctype="multipart/form-data" set correctly. Otherwise the request.FILES will be empty. It is important that the form must be submitted using the POST method.

<br>

Django can handle uploaded files easily, it has proper models such as "FileField and ImageField.<br>
The files uploaded to the FileField or ImageField are not stored in the database but in the filesystem. The FileFeld and ImageFiled, created in the database as string field (usually VARCHAR), containing the reference to the actual file. It is important to know that if you delete the string reference in the database, the actual file will not be deleted automatically, only the reference will be delete, therefore extra work needed to delete the actual file

<br>

It is important to set **MEDIA_URL** and **MEDIA_ROOT** in your project’s settings.py.

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

<br>
In the development server you may serve the user uploaded files (media) using :
<br>
Go to the primary app and open the urls.py file and add the following files<br>
<br>
>from django.conf import settings<br>
>from django.conf.urls.static import static<br>
<br>
>urlpatterns = [<br>
&emsp; # Project url patterns...<br>
]

>if settings.DEBUG:<br>
&emsp;urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

<br>

![](images/static_media.png)


<br>

--- 
### Basic File Upload (Normal way without using the Model and Forms)
Open template folder and create a new html page and name it upload.html<br>
inside that page add the following code <br>
<br>

**upload.html**<br>

`{% extends 'home.html' %}`

`{% load static %}`

`{% block content %}`<br>
 &emsp; `<form method="post" enctype="multipart/form-data">`<br>
     &emsp; &emsp;`{% csrf_token %}`<br>
     &emsp; &emsp;`<input type="file" name="myfile">`<br>
     &emsp; &emsp;`<button type="submit">Upload</button>`<br>
   &emsp;`</form>`<br>

   &emsp;`{% if uploaded_file_url %}`<br>
     &emsp; &emsp;`<p>File uploaded at: <a href="{{ uploaded_file_url }}">{{ uploaded_file_url }}</a></p>`<br>
  &emsp;`{% endif %}`<br>

   &emsp;`<p><a href="{% url 'addatt:homepage' %}">Return to home</a></p>`<br>
`{% endblock %}`<br>

<br>


Now let go to the views.py file and add the following code <br>

**views.py**<br>

`from django.shortcuts import render`<br>
`from django.conf import settings` <br>
`from django.core.files.storage import FileSystemStorage`<br>

`def uploadfl(request):`<br>
&nbsp;&nbsp;&nbsp;&nbsp;` request.method == 'POST' and request.FILES['myfile']:`<br>
&nbsp;&nbsp;&nbsp;&nbsp;` myfile = request.FILES['myfile']`<br>
&nbsp;&nbsp;&nbsp;&nbsp;` fs = FileSystemStorage()`<br>
&nbsp;&nbsp;&nbsp;&nbsp;` filename = fs.save(myfile.name, myfile)`<br>
&nbsp;&nbsp;&nbsp;&nbsp;` uploaded_file_url = fs.url(filename)`<br>
&nbsp;&nbsp;&nbsp;&nbsp;` return render(request, 'upload.html', {'uploaded_file_url': uploaded_file_url})`
&nbsp;&nbsp;&nbsp;&nbsp;` return render(request, 'upload.html')`<br>

<br>

---
### File Upload With Model Forms

---
Now, this is a way more convenient way. Model forms perform validation, automatically builds the absolute path for the upload, treats filename conflicts and other common tasks.

Inside the models.py file, add the following codes:<br>

`from django.db import models`

`class Document(models.Model):`<br>
&nbsp;&nbsp;&nbsp;&nbsp;`    description = models.CharField(max_length=255, blank=True)`<br>
&nbsp;&nbsp;&nbsp;&nbsp;`    document = models.FileField(upload_to='documents/')`<br>
&nbsp;&nbsp;&nbsp;&nbsp;`    uploaded_at = models.DateTimeField(auto_now_add=True)`<br>

<br>
here we are going to create a forms.py file, and all the code bellow to it.
**forms.py**<br>
`from django import forms`<br>
`from uploads.core.models import Document`<br>

`class DocumentForm(forms.ModelForm):`<br>
&nbsp;&nbsp;&nbsp;&nbsp;    `class Meta:`<br>
&nbsp;&nbsp;&nbsp;&nbsp;        `model = Document`<br>
&nbsp;&nbsp;&nbsp;&nbsp;        `fields = ('description', 'document', )`<br>

<br>

**views.py**<br>
`def model_form_upload(request):`<br>
&nbsp;&nbsp;&nbsp;&nbsp;    `if request.method == 'POST':`<br>
&nbsp;&nbsp;&nbsp;&nbsp;        `form = DocumentForm(request.POST, request.FILES)`<br>
&nbsp;&nbsp;&nbsp;&nbsp;        `if form.is_valid():`<br>
&nbsp;&nbsp;&nbsp;&nbsp;            `form.save()`<br>
&nbsp;&nbsp;&nbsp;&nbsp;            `return redirect('home')`<br>
&nbsp;&nbsp;&nbsp;&nbsp;    `else:`<br>
&nbsp;&nbsp;&nbsp;&nbsp;       `form = DocumentForm()`<br>
&nbsp;&nbsp;&nbsp;&nbsp;    `return render(request, 'core/model_form_upload.html', {`
&nbsp;&nbsp;&nbsp;&nbsp;        `'form': form`
&nbsp;&nbsp;&nbsp;&nbsp;    `})`<br>

<br>
<br>
<br>
<br>


<div style="background-color:#f1f1f1;padding:0 0 0 10px;color:#333;font-weigh:bold;">

## Part Five

</div>

### Migration

Django is designed to work with a relational database, stored in a relational database management system like PostgreSQL, MySQL, or SQLite.<br>
All database systems supported by Django use the language SQL to create, read, update and delete data in a relational database.

<br>
Working directly with SQL can be quite cumbersome, so to make your life easier, Django comes with an object-relational mapper, or ORM for short. The ORM maps the relational database to the world of object oriented programming. Instead of defining database tables in SQL, you write Django models in Python. Your models define database fields, which correspond to the columns in their database tables.

<br>
Here’s an example of how a Django model class is mapped to a database table:
<br>

![](images/sql1.png)

---
_source:https://realpython.com/django-migrations-a-primer/_
<br>
---
defining a model class in a Python file will not make a database. We have to make migration in order to creating the database tables. Additionally, whenever you make a change to your models, like adding a field, the database has to be changed too. Migrations handle that as well.







<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

# References to

* https://simpleisbetterthancomplex.com/tutorial/2016/08/01/how-to-upload-files-with-django.html
* https://docs.djangoproject.com/en/3.1/topics/http/file-uploads/
* https://intellipaat.com/blog/tutorial/python-django-tutorial/django-template-models-registration/
* https://realpython.com/django-migrations-a-primer/

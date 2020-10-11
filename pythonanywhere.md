# Deploying an existing Django project on PythonAnywhere

<span style="font-size:0.8rem; font-style:italic;text-decoration:underline;"> The source is: https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/ </span>
<p>
Deploying a Django project on PythonAnywhere is a lot like running a Django project on your own PC. You'll use a virtualenv, just like you probably do on your own PC, you'll have a copy of your code on PythonAnywhere which you can edit and browse and commit to version control.

The main thing that's different is that, instead of using the Django dev server with manage.py runserver and viewing your site on localhost, you'll create what we call a Web app via the Web tab in our UI, and then configure it with a WSGI file whose job is simply to import your Django project.

And then your site will be live on the real, public Internet. woo!
</p>

<p>
The steps involved are:-

* Upload your code to PythonAnywhere
* Set up a virtualenv and install Django and any other requirements
* Set up your web app using the manual config option
* Add any other setup (static files, environment variables etc)
</p>

<br>
<br>

## Upload your code to PythonAnywhere
We are going to clone our git project (There are other ways to upload your code to pythonanywhere, like for example uploading a zip file).<br>
We will assume that the code is in GitHub, all we have to do is to just clone it from the Bash Console.

> git clone https://github.com/Tabook22/Django.git

<br>

![](images/git01.png)

<div style="height:100px;">




</div>

## Configure Virtual Environment

open a new bash console<br>
type the following:<br>
`mkvirtualenv myvenv --python=/usr/bin/python3.7`
<br>
![](images/bash01.png)

When you close your pythonanywhere applicaiton and want to open and activate your virtual environment, type:<br>
`workon myvenv`

<br>
Now our virtual environment is active.
<br>
Now we need to install Django<br>

`pip install django`
<br>
![](images/bash03.png)
<br>

to check to see if django is installed type the following;<br>

`python -m django --version`
<br>

which means python open module django and check the version<br>

<div style="height:100px;">




</div>

## Setting up your Web app and WSGI file
t this point, you need to be armed with 3 pieces of information:

* The path to your Django project's top folder -- the folder that contains "manage.py", eg /home/myusername/mysite
* The name of your project (that's the name of the folder that contains your settings.py), eg mysite
* The name of your virtualenv, eg mysite-virtualenv


<br>

### Create a Web app with Manual Config
Head over to the Web tab and create a new web app, choosing the "Manual Configuration" option and the right version of Python (the same one you used to create your virtualenv).<br>

![](images/newapp.png)
<br>

![](images/newapp2.png)
<br>
Select Django
<br>
<br>
<br>
<br>
![](images/newapp3.png)
<br>
<div style="height:100px;">
Here we are going to select the python version, for example we are going to select python 3.7
<br>
<br>
<br>
<br>

![](images/newapp4.png)

Here we are going to choose our project name, for example "StudentPro" offcourse you can choose any project name you want. 
<br>
<br>
<br>
<br>


### Enter your virtualenv name
Once that's done, enter the name of your virtualenv in the Virtualenv section on the web tab and click OK.

![](images/newapp5.png)
<br>
<br>
![](images/newapp6.png)
add the virtual environment, you created in our example the virtual environment is "myvenv"
<br>
<br>
![](images/newapp07.png)
<br>
<br>
If every thing works fine you can click on Reload button and
<br>

![](images/newapp08.png)
<br>
<br>
If there is no error you will see the following webpage
<br>
![](images/newapp09.png)
<br>

--- 
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

# Creating a new Django project on PythonAnywhere

Here we are going to create a Django project from secrach, not deploying it like what we did in the previous section above.

## Configure Virtual Environment
The first thing we need to do is to configure a new virtual environment<br>
open a new bash console<br>
type the following:<br>
`mkvirtualenv myvenv --python=/usr/bin/python3.7`
<br>

<br>



When you close your pythonanywhere applicaiton and want to open and activate your virtual environment, type:<br>
`workon myvenv`

<br>
Now our virtual environment is active.
<br>
Now we need to install Django<br>

`pip install django`

<br>

to check to see if django is installed type the following;<br>

`python -m django --version`
<br>

which means python open module django and check the version

<br>

now we are going to start our django project<br>
`django-admin startproject myproject`<br>

"myproject" is the name of the project which i want to start

<br>
now change your diractory into "myproject" <br>

`cd myproject`

<br>

now we are going to start our first app in that project (myproject)<br>

`django-admin startapp myapp`

<br>


#


Now , we have to go to the web from our dashboard and do the following steps:<br>
* change the virtual environment to the new virtual environment we just created 
  ![](images/py02.png)
* we need also to change the source code, to point to our application "myapp"<br>
  ![](images/py01.png)
* Go to wsgi.py configuration file and past the following code their<br>
  `# +++++++++++ DJANGO +++++++++++`<br>
`# To use your own Django app use code like this:`<br>
`import os`<br>
`import sys`<br>
<br>

`# assuming your Django settings file is at '/home/myusername/mysite/mysite/settings.py'`<br>
`path = '/home/myusername/mysite'`<br>
`if path not in sys.path:`<br>
`    sys.path.insert(0, path)`<br>
<br>

`os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'`<br>

<br>

`## Uncomment the lines below depending on your Django version`<br>
`###### then, for Django >=1.5:`<br>
`from django.core.wsgi import get_wsgi_application`<br>
`application = get_wsgi_application()`<br>
`###### or, for older Django <=1.4`<br>
`#import django.core.handlers.wsgi`<br>
`#application = django.core.handlers.wsgi.WSGIHandler()`<br>

then we have to do change  "mysite.settings" to myproject.settings, and "path='/home/muusername/mysite'" to path='/home/tabook22/myproject'<br>
<br>
the username in my case is tabook22, and the name of the project is myproject
<br>

the next last step , go to your settings.py file and change the ALLOWED_HOSTS=[] to ALLOWED_HOSTS=['tabook22.pythonanywhere.com'], this is my website, it just my username and the pythonanywhere.com. <br>

also go the INSTALLED_APPS and add the name of your application you just created which is called "myapp"
# Deploy to Pythonanywhere (using zip file method)

Create a zip file of your project.

![](images/zip.png)
here for example yoj can select the inner folders, and not the main folder "DUAtt" <br>
select the following folders and put them in one zip file<br>
* addatt
* DUAtt
* media
* template
* manage.py

these folders and files will be in one zip file and then from within your pythonanywhere project you upload them <br>

![](images/zip2.png)
<br>
First thing befor uploading the zip file and unzip its contents, you have go to pythonanywhere and create a new web application<br>

![](images/newapp.png)
<br>
follow the instructions, and make sure to name the project as the zip file name, for example if the zip file name is "DUAtt" Then the project also named "DUAtt"
<br>
go to the project (from files) open it, and inside the project folder, upload the project zip file
then open console from within the same folder
Tyep unzip project.zip file and if there any message appears regarding overwritte choose All.
<br>

after unziping the project folder, open it and go to the settings file and do the following changes<br>
`#SECURITY WARNING: don't run with debug turned on in production!`<br>
`DEBUG = False`<br>
`# Static files (CSS, JavaScript, Images)`<br>
`# https://docs.djangoproject.com/en/2.1/howto/static-files/`<br>

`STATIC_URL = '/static/`

`# default static files settings for PythonAnywhere.`<br>
`# see https://help.pythonanywhere.com/pages/DjangoStaticFiles for more info`<br>
`PROJECT_DIR=os.path.dirname(os.path.abspath(__file__))`<br>
`MEDIA_ROOT = os.path.join(PROJECT_DIR,'media')`<br>
`MEDIA_URL = '/media/'`<br>
`STATIC_ROOT = os.path.join(PROJECT_DIR,'static')`<br>
`STATIC_URL = '/static/'`<br>

<br>

![](images/static.png)
<br>
after that go the console, and issue the following command to collect all static files<br>
`python3.7 manage.py collectstatic`<br>

![](images/static2.png)


then copy the static file folder, which appears in the console, and go to the web applicaiotn table and change the static file folder in the static files section.<br>

![](images/static3.png)

![](images/static4.png)

reload the webpage and open it.
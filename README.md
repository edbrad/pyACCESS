# pyACCESS
Django/Python MS ACCESS Data Access Demo Web Application

The purpose of this application is to demonstrate the ability to externaly access the EMS Legacy MS ACCESS databases.  
This application is built using **Django**, a *Python-based* Web application framework.

This application currently utilizes the **pyodbc** Python library to connect and read from the MS Access Database (.mdb).

This Application is being primarily developed and maintained in a **Windows** (Windows 10) environment using **Visual Studio Code** (VSCODE).

## Clone inital Github repository

~~~~
C:\py>git clone https://github.com/edbrad/pyACCESS.git
Cloning into 'pyACCESS'...
remote: Counting objects: 8, done.
remote: Compressing objects: 100% (8/8), done.
remote: Total 8 (delta 1), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (8/8), done.
~~~~

## Create and Activate Python Virtual Environment 
Limit the scope of the Application's dependent packages (the Application's "venv" folder in this case). 
The *activate* script must be run to enable the created Virtual Environment.

~~~~
C:\py>cd pyACCESS

C:\py\pyACCESS>virtualenv venv
Using base prefix 'c:\\program files (x86)\\python35-32'
New python executable in C:\py\pyACCESS\venv\Scripts\python.exe
Installing setuptools, pip, wheel...done.
~~~~
~~~~
C:\py\pyACCESS> venv\Scripts\activate

(venv) C:\py\pyACCESS>
~~~~ 

## Install Django Framework
Use Python package manager (pip) to download and install the latest version of **Django**.

~~~~
(venv) C:\py\pyACCESS>pip install django
Collecting django
  Using cached Django-1.10.4-py2.py3-none-any.whl
Installing collected packages: django
Successfully installed django-1.10.4
~~~~

## Initialize Django Project
Create a Parent Project (pyACCESS) for Application(s). Test the initial functionality.

~~~~
(venv) C:\py\pyACCESS>django-admin startproject pyACCESS
~~~~

~~~~
(venv) C:\py\pyACCESS\pyACCESS>python manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).

You have 13 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
December 11, 2016 - 21:07:44
Django version 1.10.4, using settings 'pyACCESS.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
~~~~

## Create first App within the Project
Create the first (main) Application under the parent Project.

~~~~
(venv) C:\py\pyACCESS\pyACCESS>python manage.py startapp www
~~~~

## Register the new App with Django
Update the Django Project's *settings.py* file to register the new App (www).

~~~~
# Application definition

INSTALLED_APPS = [
    'www',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
~~~~

## Bootstrap new App
Wire up code to display basic web page from App.

**Add Python linting (pylint) support in VS Code**: 

*File --> Preferences --> Workspace Settings* (.vscode\settings.json).

~~~~
// Place your settings in this file to overwrite default and user settings.
{
    "python.linting.pylintArgs": ["--load-plugins", "pylint_django"]
}
~~~~

**Add code for initial view**

www\views.py
~~~~
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
~~~~

create new *templates* folder under the App (www) folder to hold HTML template files (must be named "templates").

www\templates\index.html 
~~~~
<!DOCTYPE html>
<html>
    <head>
        <title>pyACCESS</title>
    </head>
    <body>
        <h1>pyACCESS</h1>
    </body>
</html>
~~~~

create a urls.py file in the new App directory (www).
~~~~
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
]
~~~~

add a reference/link in the Project's url file (pyAccess\urls.py) to the new url file in the child App (www). 
the *include* library must be referenced.
~~~~
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('www.urls')),
]
~~~~

## Add MS Jet/ACCESS support (pyodbc)

install pyodbc library (pip).  
~~~~
(venv) C:\py\pyACCESS>pip install pyodbc
Collecting pyodbc
  Using cached pyodbc-3.1.1-cp35-cp35m-win32.whl
Installing collected packages: pyodbc
Successfully installed pyodbc-3.1.1
~~~~

import the library (in pyACCESS\views.py)
~~~~
import pyodbc # Python ODBC Library (ACCESS 97 connectivity)
~~~~




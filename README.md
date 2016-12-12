# pyACCESS
Django/Python MS ACCESS Data Access Demo Web Application

The purpose of this application is to demonstrate the ability to externaly access the EMS Legacy MS ACCESS databases.  
This application is built using **Django**, a *Python-based* Web application framework.

This application currently utilizes the **django-pyodbc-access** open-source library (https://bitbucket.org/jkafader/django-pyodbc-access).

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
Use Python package manager (pip) to download and install the latest version of **Django**

~~~~
(venv) C:\py\pyACCESS>pip install django
Collecting django
  Using cached Django-1.10.4-py2.py3-none-any.whl
Installing collected packages: django
Successfully installed django-1.10.4
~~~~
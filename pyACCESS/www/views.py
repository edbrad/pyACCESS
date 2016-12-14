from django.shortcuts import render
import pyodbc # Python ODBC Library (ACCESS 97 connectivity)

# Create your views here.
def index(request):
    return render(request, 'index.html')

def joblist(request):
    return render(request, 'joblist.html')
from django.shortcuts import render
import pyodbc # Python ODBC Library (ACCESS 97 connectivity)

# Create your views here.
def index(request):
    return render(request, 'index.html')

def joblist(request):
    jobnum = request.GET['jobnum']
    cnxn = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb)};Dbq=C:\\data\\mdb\\Jtk2002_Data.mdb;")
    crsr = cnxn.cursor()
    crsr.execute("SELECT * FROM Comp_Job where Jobnum like ?", (str(jobnum) + "%"))
    rows = crsr.fetchall()
    cnxn.close()
    return render(request, 'joblist.html', {"rows": rows})
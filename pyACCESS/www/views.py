from django.shortcuts import render
import pyodbc # Python ODBC Library (ACCESS 97 connectivity)



# Create your views here.
def index(request):
    cnxn = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb)};Dbq=C:\\data\\mdb\\Jtk2002_Data.mdb;")
    crsr = cnxn.cursor()
    crsr.execute("SELECT * FROM Comp_Job where Jobnum like ?", ("9999" + "%"))
    rows = crsr.fetchall()
    cnxn.close()
    return render(request, 'index.html', {'rows':rows})
    
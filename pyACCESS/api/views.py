from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import datetime
import collections
import pyodbc # Python ODBC Library (ACCESS 97 connectivity)

# API Welcome Response
@api_view(['GET'])
def root(request):
    """
    Generic/Default Text Response.
    """
    data = 'Welcome to the pyACCESS REST API'
    return Response(data)

# get list of jobs
@api_view(['GET'])
def joblist(request, jobnum):
    """
    Query the ACCESS Database and return the list of matching Jobs (jobnum)
    """
    if jobnum == "":
        rows = None
    else:
        cnxn = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb)};Dbq=C:\\data\\mdb\\Jtk2002_Data.mdb;")
        crsr = cnxn.cursor()
        crsr.execute("SELECT * FROM Comp_Job where Jobnum like ?", (str(jobnum) + "%"))
        rows = crsr.fetchall()

        cnxn.close()
    
    """
    Serialize the query results into JSON (via a Python dictionary collection)
    """
    joblist = list()
    for row in rows:
        d = collections.OrderedDict()
        d['Jobnum'] = row.Jobnum
        d['Company'] = row.Company
        d['JobDescp'] = row.JobDescp
        d['Remark'] = row.Remark
        d['DropDate'] = row.DropDate
        d['ToDropDate'] = row.ToDropDate
        d['Permit'] = row.Permit
        joblist.append(d)

    """
    Return the response data (JSON)
    """
    return Response(joblist)
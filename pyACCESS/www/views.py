from django.shortcuts import render
import pyodbc # Python ODBC Library (ACCESS 97 connectivity)

# root/job # search
def index(request):
    return render(request, 'index.html')

# display list of jobs (from index/search form GET)
def joblist(request):
    jobnum = request.GET['jobnum']
    if jobnum == "":
        rows = None
    else:
        cnxn = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb)};Dbq=C:\\data\\mdb\\Jtk2002_Data.mdb;")
        crsr = cnxn.cursor()
        crsr.execute("SELECT * FROM Comp_Job where Jobnum like ?", (str(jobnum) + "%"))
        rows = crsr.fetchall()
        cnxn.close()
        
    return render(request, 'joblist.html', {"rows": rows, "jobnum": jobnum})

# display details for selected job number (from joblist)
def jobdetails(request, jobnum):
    if jobnum == "":
        rows = None
    else:
        # get info for the selected Job #
        cnxn = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb)};Dbq=C:\\data\\mdb\\Jtk2002_Data.mdb;")
        crsr = cnxn.cursor()
        crsr.execute("SELECT * FROM Comp_Job where Jobnum = ?", (str(jobnum)))
        rows = crsr.fetchall()
        
        # get pattern info for the selected Job 
        crsr_2 = cnxn.cursor()
        crsr_2.execute("SELECT * FROM [Job Details] where jobnum = ?", (str(jobnum)))
        patterns = crsr_2.fetchall()
        cnxn.close()
        
        total_pattern_count = 0
        total_job_count = 0
        for pat in patterns:
            total_pattern_count = (int(pat.PackShip) + int(pat.cbas) + int(pat.cpre) + int(pat.ccrt) +
                              int(pat.cwalk125) + int(pat.csat) + int(pat.cbasbar) + int(pat.cdig3bar) +
                              int(pat.cdig5bar) + int(pat.caadc) + int(pat.cmaadc) + int(pat.cbas3dig) +
                              int(pat.foreign) + int(pat.canadian))
                              
            # overwrite the NSA field (outdated) with the total piece count for the pattern
            # types of <pyodbc.Row> do not expose an .append method
            pat.lngNSAID = total_pattern_count

            total_job_count = total_job_count + total_pattern_count

    return render(request, 'jobdetails.html', {"rows": rows, 
                                               "jobnum": jobnum, 
                                               "patterns": patterns,
                                               "totjobcount": total_job_count
                                               })
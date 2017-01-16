from django.shortcuts import render
import pyodbc # Python ODBC Library (ACCESS 97 connectivity)
import re # Python regular expressions library

# root/job # search
def index(request):
    return render(request, 'index.html')

# display list of jobs (from index/search form GET)
def joblist(request):
    jobnum = request.GET['jobnum']
    if jobnum == "":
        rows = None
    else:
        #cnxn = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb)};Dbq=C:\\data\\mdb\\Jtk2002_Data.mdb;")
        cnxn = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb)};Dbq=\\FS-0\\sys\\dbsys\\JobTicket\\Jtk2002_Data.mdb;")
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
        #cnxn = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb)};Dbq=C:\\data\\mdb\\Jtk2002_Data.mdb;")
        cnxn = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb)};Dbq=\\FS-0\\sys\\dbsys\\JobTicket\\Jtk2002_Data.mdb;")
        crsr = cnxn.cursor()
        crsr.execute("SELECT * FROM Comp_Job where Jobnum = ?", (str(jobnum)))
        job = crsr.fetchone()
        
        # get pattern info for the selected Job 
        crsr_2 = cnxn.cursor()
        crsr_2.execute("SELECT * FROM [Job Details] where jobnum = ?", (str(jobnum)))
        patterns = crsr_2.fetchall()

        # get the Company address for the Job Number
        crsr_3 = cnxn.cursor()
        crsr_3.execute("SELECT * FROM COMPANY where Comp = ? AND Contact = ?", (str(job.Company), str(job.Contact)))
        company = crsr_3.fetchone()
        # clean/reformat Company fields for better display
        if company:
            if company.Add2 == None:
                company.Add2 = " "
            if company.phone == None:
                company.phone = " "
            if company.phone != None and company.phone != " ":
                company.phone = format_phone(company.phone)

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

    return render(request, 'jobdetails.html', {"jobnum": jobnum, 
                                               "patterns": patterns,
                                               "totjobcount": total_job_count,
                                               "job": job,
                                               "company": company
                                               })

# display details for selected pattern (from jobdetails)
def patterndetails(request, jobnum, pattern):
    if (jobnum == "" or pattern == ""):
        patterns = None
    else:
        # get pattern info for the selected Job #
        #cnxn = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb)};Dbq=C:\\data\\mdb\\Jtk2002_Data.mdb;")
        cnxn = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb)};Dbq=\\FS-0\\sys\\dbsys\\JobTicket\\Jtk2002_Data.mdb;")
        crsr_2 = cnxn.cursor()
        crsr_2.execute("SELECT * FROM [Job Details] where jobnum = ? AND jobpat = ?", (str(jobnum), str(pattern)))
        patterns = crsr_2.fetchall()

        cnxn.close()

        total_pattern_count = 0
        for pat in patterns:
            total_pattern_count = (int(pat.PackShip) + int(pat.cbas) + int(pat.cpre) + int(pat.ccrt) +
                                  int(pat.cwalk125) + int(pat.csat) + int(pat.cbasbar) + int(pat.cdig3bar) +
                                  int(pat.cdig5bar) + int(pat.caadc) + int(pat.cmaadc) + int(pat.cbas3dig) +
                                  int(pat.foreign) + int(pat.canadian))   

    return render(request, 'patterndetails.html', {"patterns": patterns, "jobnum": jobnum, "pattern": pattern, 
                           'patterntotal': total_pattern_count})


# reformat phone numbers
def format_phone(phone_number):
    # strip non-numeric characters
    phone = re.sub(r'\D', '', phone_number)
    # remove leading 1 (area codes never start with 1)
    phone = phone.lstrip('1')
    return '({}) {}-{}'.format(phone[0:3], phone[3:6], phone[6:])
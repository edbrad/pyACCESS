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

# Search for Job(s) by Job Number (full or partial)
@api_view(['GET'])
def jobnum_search(request):
    """
    Search the ACCESS Database and return the list of matching Jobs with general Job information
    """
    jobnum = request.GET['jobnum'] # get the job number parameter from the http request
    
    if jobnum == "":
        rows = None
    else:
        #cnxn = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb)};Dbq=C:\\data\\mdb\\Jtk2002_Data.mdb;")
        cnxn = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb)};Dbq=\\FS-0\\sys\\dbsys\\JobTicket\\Jtk2002_Data.mdb;")
        crsr = cnxn.cursor()
        crsr.execute("SELECT * FROM Comp_Job where Jobnum like ?", (str(jobnum) + "%"))
        rows = crsr.fetchall()
        # close the connection/lock
        cnxn.close()
    
    """
    Serialize the query results into JSON (via a Python dictionary collection)
    """
    joblist = list()
    for row in rows:
        # build list entry
        d = collections.OrderedDict()
        d['Jobnum'] = row.Jobnum
        d['Company'] = row.Company
        d['DateReceived'] = row.DateReceived 
        d['DropDate'] = row.DropDate
        d['ToDropDate'] = row.ToDropDate
        d['JobTicketDate'] = row.__getattribute__('Job Ticket Date')
        d['JobDescp'] = row.JobDescp
        d['RDept'] = row.RDept
        d['Sample1'] = row.Sample1
        d['Sample2'] = row.Sample2
        d['Sample3'] = row.Sample3
        d['Sample4'] = row.Sample4
        d['Sample5'] = row.Sample5
        d['Sample6'] = row.Sample6
        d['Sample7'] = row.Sample7
        d['Sample8'] = row.Sample8
        d['Sample9'] = row.Sample9
        d['Sample10'] = row.Sample10
        d['Sample11'] = row.Sample11
        d['Sample12'] = row.Sample12
        d['Sample13'] = row.Sample13
        d['Sample14'] = row.Sample14
        d['Sample15'] = row.Sample15
        d['Sample16'] = row.Sample16
        d['Sample17'] = row.Sample17
        d['Sample18'] = row.Sample18
        d['Sample19'] = row.Sample19
        d['Sample20'] = row.Sample20
        d['Sample21'] = row.Sample21
        d['Sample22'] = row.Sample22
        d['PostageBy'] = row.PostageBy
        d['stockInst'] = row.stockInst
        d['CRInst'] = row.CRInst
        d['MeterInst'] = row.MeterInst
        d['BDInst'] = row.BDInst
        d['AdDept'] = row.AdDept
        d['InDInst'] = row.InDInst
        d['PO3602Inst'] = row.__getattribute__('3602Inst')
        d['Remark'] = row.Remark
        d['PO'] = row.PO
        d['Permit'] = row.Permit
        d['Spoilage'] = row.Spoilage
        d['StampInst'] = row.StampInst
        d['ysnReports'] = row.ysnReports
        # add entry to the list
        joblist.append(d)

    """
    Return the response data (JSON)
    """
    return Response(joblist)

# Get pattern details for selected job number
@api_view(['GET'])
def jobdetails(request):
    """
    Query the ACCESS Database and return the list of matching Job Details (Patterns)
    """
    jobnum = request.GET['jobnum'] # get the job number parameter from the http request
    
    if jobnum == "":
        rows = None
    else:
        # get pattern details for the selected Job
        #cnxn = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb)};Dbq=C:\\data\\mdb\\Jtk2002_Data.mdb;")
        cnxn = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb)};Dbq=\\FS-0\\sys\\dbsys\\JobTicket\\Jtk2002_Data.mdb;") 
        crsr = cnxn.cursor()
        crsr.execute("SELECT * FROM [Job Details] where jobnum = ?", (str(jobnum)))
        rows = crsr.fetchall()
        # close the connection/lock
        cnxn.close()

        """
        Serialize the query results into JSON (via a Python dictionary collection)
        """
        patlist = list()
        for row in rows:
            # build list entry
            d = collections.OrderedDict()
            d['Jobnum'] = row.jobnum
            d['Jobpat'] = row.jobpat
            d['MailClass'] = row.MailClass
            d['DESCP1'] = row.DESCP1
            d['DESCP2'] = row.DESCP2
            d['DESCP3'] = row.DESCP3
            d['DESCP4'] = row.DESCP4
            d['DESCP5'] = row.DESCP5
            d['DESCP6'] = row.DESCP6
            d['PostName1'] = row.PostName1
            d['PostCode1'] = row.PostCode1
            d['PostNote1'] = row.PostNote1
            d['OuterName'] = row.OuterName
            d['OuterCode'] = row.OuterCode
            d['OuterNote'] = row.OuterNote
            d['Insert1Name'] = row.Insert1Name
            d['Insert1Code'] = row.Insert1Code
            d['Insert1Note'] = row.Insert1Note
            d['Insert2Name'] = row.Insert2Name
            d['Insert2Code'] = row.Insert2Code
            d['Insert2Note'] = row.Insert2Note
            d['Insert3Name'] = row.Insert3Name
            d['Insert3Code'] = row.Insert3Code
            d['Insert3Note'] = row.Insert3Note
            d['Insert4Name'] = row.Insert4Name
            d['Insert4Code'] = row.Insert4Code
            d['Insert4Note'] = row.Insert4Note
            d['Insert5Name'] = row.Insert5Name
            d['Insert5Code'] = row.Insert5Code
            d['Insert5Note'] = row.Insert5Note
            d['Insert6Name'] = row.Insert6Name
            d['Insert6Code'] = row.Insert6Code
            d['Insert6Note'] = row.Insert6Note
            d['Insert7Name'] = row.Insert7Name
            d['Insert7Code'] = row.Insert7Code
            d['Insert7Note'] = row.Insert7Note
            d['Insert8Name'] = row.Insert8Name
            d['Insert8Code'] = row.Insert8Code
            d['Insert8Note'] = row.Insert8Note
            d['Insert9Name'] = row.Insert9Name
            d['Insert9Code'] = row.Insert9Code
            d['Insert9Note'] = row.Insert9Note
            d['Insert10Name'] = row.Insert10Name
            d['Insert10Code'] = row.Insert10Code
            d['Insert10Note'] = row.Insert10Note
            d['Insert11Name'] = row.Insert11Name
            d['Insert11Code'] = row.Insert11Code
            d['Insert11Note'] = row.Insert11Note
            d['Insert12Name'] = row.Insert12Name
            d['Insert12Code'] = row.Insert12Code
            d['Insert12Note'] = row.Insert12Note
            d['Insert13Name'] = row.Insert13Name
            d['Insert13Code'] = row.Insert13Code
            d['Insert13Note'] = row.Insert13Note
            d['Insert14Name'] = row.Insert14Name
            d['Insert14Code'] = row.Insert14Code
            d['Insert14Note'] = row.Insert14Note
            d['Insert15Name'] = row.Insert15Name
            d['Insert15Code'] = row.Insert15Code
            d['Insert15Note'] = row.Insert15Note
            d['Insert16Name'] = row.Insert16Name
            d['Insert16Code'] = row.Insert16Code
            d['Insert16Note'] = row.Insert16Note
            d['Insert17Name'] = row.Insert17Name
            d['Insert17Code'] = row.Insert17Code
            d['Insert17Note'] = row.Insert17Note
            d['Insert18Name'] = row.Insert18Name
            d['Insert18Code'] = row.Insert18Code
            d['Insert18Note'] = row.Insert18Note
            d['Insert19Name'] = row.Insert19Name
            d['Insert19Code'] = row.Insert19Code
            d['Insert19Note'] = row.Insert19Note
            d['Insert20Name'] = row.Insert20Name
            d['Insert20Code'] = row.Insert20Code
            d['Insert20Note'] = row.Insert20Note
            d['Insert21Name'] = row.Insert21Name
            d['Insert21Code'] = row.Insert21Code
            d['Insert21Note'] = row.Insert21Note
            d['Insert22Name'] = row.Insert22Name
            d['Insert22Code'] = row.Insert22Code
            d['Insert22Note'] = row.Insert22Note
            d['Insert23Name'] = row.Insert23Name
            d['Insert23Code'] = row.Insert23Code
            d['Insert23Note'] = row.Insert23Note
            d['Insert24Name'] = row.Insert24Name
            d['Insert24Code'] = row.Insert24Code
            d['Insert24Note'] = row.Insert24Note
            d['Insert25Name'] = row.Insert25Name
            d['Insert25Code'] = row.Insert25Code
            d['Insert25Note'] = row.Insert25Note
            d['Payment'] = row.Payment
            d['PackShip'] = row.PackShip
            d['cbas'] = row.cbas
            d['cpre'] = row.cpre
            d['ccrt'] = row.ccrt
            d['cwalk125'] = row.cwalk125
            d['csat'] = row.csat
            d['cbasbar'] = row.cbasbar
            d['cdig3bar'] = row.cdig3bar
            d['cdig5bar'] = row.cdig5bar
            d['caadc'] = row.caadc
            d['cmaadc'] = row.cmaadc
            d['cbas3dig'] = row.cbas3dig
            d['foreign'] = row.foreign
            d['canadian'] = row.canadian
            d['lngNSAID'] = row.lngNSAID
            d['lngEPOPtype'] = row.lngEPOPtype
            d['ysnBagTagsDone'] = row.ysnBagTagsDone
            d['dtmBagTagsDone'] = row.dtmBagTagsDone 
            # add entry to the list
            patlist.append(d)

        """
        Return the response data (JSON)
        """
        return Response(patlist)

# Get Companies
@api_view(['GET'])
def companies(request):
    """
    Query the ACCESS Database and return the list of Companies with Company details
    """
    # get all the Companies
    #cnxn = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb)};Dbq=C:\\data\\mdb\\Jtk2002_Data.mdb;")
    cnxn = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb)};Dbq=\\FS-0\\sys\\dbsys\\JobTicket\\Jtk2002_Data.mdb;")
    crsr = cnxn.cursor()
    crsr.execute("SELECT * FROM [COMPANY]")
    rows = crsr.fetchall()
    # close the connection/lock
    cnxn.close()

    """
    Serialize the query results into JSON (via a Python dictionary collection)
    """
    companylist = list()
    for row in rows:
        # build list entry
        d = collections.OrderedDict()
        d['Comp'] = row.Comp
        d['Contact'] = row.Contact
        d['Add1'] = row.Add1
        d['Add2'] = row.Add2
        d['City'] = row.City
        d['state'] = row.state
        d['zip'] = row.zip
        d['phone'] = row.phone
        # add entry to the list
        companylist.append(d)

    """
    Return the response data (JSON)
    """
    return Response(companylist)
from django.shortcuts import render
from .import pool
import ast
from django.views.decorators.clickjacking import xframe_options_exempt
import json
from django.http import JsonResponse
from urllib.parse import unquote
def Action_Registration(request):
   return render(request,"Registration.html")
def Submit_Record(request):
   try:
     DB,CMD=pool.ConnectionPooling()
     cdname=request.POST['cdname']
     cdmail=request.POST['cdmail']
     cddob=request.POST['cddob']
     cdcontact=request.POST['cdcontact']
     cdinst=request.POST['cdinst']
     cdpwd=request.POST['cdpwd']
     ccdpwd=request.POST['ccdpwd']
     if(cdpwd==ccdpwd):
      Q="insert into cddetails(cdname,cdmail,cddob,cdcontact,cdinst,cdpwd,ccdpwd) values('{0}','{1}','{2}','{3}','{4}','{5}','{6}')".format(cdname,cdmail,cddob,cdcontact,cdinst,cdpwd,ccdpwd)
      CMD.execute(Q)
      DB.commit()
      DB.close()
      return render(request,'Registration.html',{'message':'Record Submited'})
     else:
        return render(request,'Registration.html',{'message':'Both Password are Different Try Again'})
   except Exception as d:
      print('Error:',d)
      return render(request,'Registration.html',{'message':'Record Faild'})
@xframe_options_exempt
def DisplayAllRecords(request):
    try:
        admin=request.session['ADMIN']
    except:
     return render(request,"AdminLogIn.html")
    try:
         DB, CMD = pool.ConnectionPooling()
         Q = "select * from cddetails"
         print(Q)
         CMD.execute(Q)
         records = CMD.fetchall()
         DB.close()
         return render(request, 'DisplayRecordsAdmin.html', {'records': records})
    except Exception as d:
         return render(request, 'DisplayRecordsAdmin.html', {'records': None})
@xframe_options_exempt
def Action_StartQuiz(request):
    return render(request,'StartQuiz.html')

from django.shortcuts import render
from .import pool
from django.http import JsonResponse
def Action_LogIn(request):
   return render(request,"AdminLogIn.html")
def AdminLogIn_Check(request):
  try:
     DB,CMD=pool.ConnectionPooling()
     emailid=request.POST['emailid']
     psw=request.POST['password']
     Q="select * from adminlogin where emailid='{0}' and password='{1}'".format(emailid,psw)
     print(Q)
     CMD.execute(Q)
     row=CMD.fetchone()
     if(row):
        request.session['ADMIN']=row
        return render(request, 'AdminDashBoard.html',{'AdminData':row})
     else:
        return render(request, 'AdminLogIn.html', {'message': 'Invalid User Id/Password'})
     DB.close()
  except Exception as d:
      print("Error",d)
      return render(request, 'AdminLogIn.html', {'message': 'Something Went Wrong'})
def Admin_LogOut(request):
    del request.session['ADMIN']
    return render(request,'AdminLogIn.html')
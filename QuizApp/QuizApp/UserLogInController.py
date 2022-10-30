from django.shortcuts import render
from .import pool
from django.http import JsonResponse
from django.views.decorators.clickjacking import xframe_options_exempt

def Action_LogIn(request):
   return render(request,"UserLogIn.html")
# def User_LogOut(request):
#     del request.session['USER']
#     return render(request,'UserLogIn.html')
data=dict()
def UserLogIn_Check(request):
  try:
     DB,CMD=pool.ConnectionPooling()
     emailid=request.POST['emailid']
     psw=request.POST['password']
     Q="select * from cddetails where cdmail='{0}' && cdpwd='{1}'".format(emailid,psw)
     print(Q)
     CMD.execute(Q)
     row=CMD.fetchone()
     if(row):
        print(row)
        print(type(row))
        # request.session['USER']=row
        return render(request, 'UserDashBoard.html',{'UserData':row })
     else:
        return render(request, 'UserLogIn.html', {'message': 'Invalid User Id/Password'})
     DB.close()
  except Exception as d:
      print("Error",d)
      return render(request, 'UserLogIn.html', {'message': 'Something Went Wrong'})

@xframe_options_exempt
def Action_ScoreBoard(request):
        print(data)
        return render(request, 'ScoreBoard.html',{'UserData':data})
# def Action_SubmitAns(request):
#     CMD
#     return render(request,'StartQuiz.html')




from django.shortcuts import render,redirect
from django.http import HttpResponse
from addapp.models import Faculty,Feedback,Register
def login(request):
	return render(request,"faculty/login.html")
def loginlogic(request):
	res=Faculty.objects.filter(emailid=request.POST["txtemail"],password=request.POST["txtpass"])
    
	if(res):
	 request.session['fid'] = request.POST["txtemail"]
	 return redirect("dashboard")
	else:
	 return render(request,"faculty/login.html",{'msg':"Invalid Userid and Password"}) 
def dashboard(request):
	s=request.session['fid']
	data = Feedback.objects.filter(feedto=s)
	return render(request,"faculty/dashboard.html",{'res':data})
def logout(request):
	del request.session['fid']
	return redirect('login')
def searchstudent(request):
	return render(request,"faculty/searchstudent.html")
def searchstu(request):
	s=request.GET["q"]
	result = Register.objects.filter(fullname__contains=s)
	return render(request,"faculty/searchstu.html",{'res':result})
	

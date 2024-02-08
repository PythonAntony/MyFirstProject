from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, "home.html")
def about(request):
    return HttpResponse("<h1 style='text-align:center;'>Welcome to all to know about our firm</h1>")
def contact(request):
    return render(request, "contact.html")
def details(request):
    return HttpResponse("<h1 style='text-align:center;'>Browse more details about us to know more about us </h1>")
def thanx(request):
    return render(request, "thanx.html")
def valuerepl(request):
    name="Friends"
    return render(request,"ValueReplacement.html",{'obj':name})
def addition(request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    resA = x + y
    resS = x - y
    resM = x * y
    resD = x / y
    return render(request,"result.html",{'no1':x,'no2':y,'resultA':resA,'resultS':resS,'resultM':resM,'resultD':resD})

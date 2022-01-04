from django.shortcuts import render
from django.http import  HttpResponse
# Create your views here.
def input(request):
    return render(request,'input.html')
def result(request):
    try:
        x = int(request.GET["t1"])
        y = int(request.GET["t2"])
        ope = request.GET["t3"]
        data = ""
        if ope == "add":
            z = x+y
            data = "The sum is:"+str(z)
        elif ope == "sub":
            z = x-y
            data = "The sub is:"+str(z)
        elif ope == "mul":
            z = x*y
            data = "The mul is:"+str(z)
        elif ope == "div":
            z = x/y
            data = "The div is:"+str(z)

        con_dic = {'res': data}
        return render(request, 'display.html', con_dic)
    except(ValueError):
        return render(request, 'input.html')
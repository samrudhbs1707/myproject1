from django.shortcuts import render

# def home(request,id=None):
#     if id==1:
#         return render(request, "<h1>Hello, world!</h1>")
#     if id==2:
#         return render(request, "<h1>this is django</h1>")
    
def home(request):
    return render(request,'home.html')
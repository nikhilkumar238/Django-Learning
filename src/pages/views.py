from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_view(request,*args, **kwargs): 
    # print(args, kwargs)
    print(request)
    # return HttpResponse("<h1>Hello</h1>")
    my_context ={
        "test1":"test1 value",
        "test2": "test2 value",
        "list": [122,33,2,22],
        "is_true":True
    }
    return render(request, "home.html", my_context)
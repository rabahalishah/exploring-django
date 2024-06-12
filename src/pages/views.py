from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home_view(request, *args, **kwargs):
    print("args, kwargs: ", args, kwargs)
    print("REQUEST: ", request)
    my_context = {
        "about_home": "This is my home",
        "more_information": "This house is located in Los angelas",
        "my_list": [12, 13, 14, 15]
    }
    return render(request, "home.html", my_context)


def contact_view(request, *args, **kwargs):
    print("args, kwargs: ", args, kwargs)
    print("REQUEST: ", request)
    print(args, kwargs)
    my_context = {
        "about_us": "This is about us"

    }
    return render(request, "contact.html", my_context)

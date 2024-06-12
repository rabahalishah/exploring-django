from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    print("args, kwargs: ", args, kwargs)
    print("REQUEST: ", request)
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    print("args, kwargs: ", args, kwargs)
    print("REQUEST: ", request)
    print(args, kwargs)

    return render(request, "contact.html", {})

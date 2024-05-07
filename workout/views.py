from django.shortcuts import render

def home(request):
    message = "Hello World I am learning Django"
    template = "home.html"
    context = {
        'message':message,
    }
    return render(request, template, context)
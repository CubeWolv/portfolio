from django.shortcuts import render

# Create your views here.
def webdev(request):
    return render(request, './webdev/webdev.html')
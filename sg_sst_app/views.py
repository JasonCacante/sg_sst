from django.shortcuts import render

def home(request):
    return render(request, "sg_sst_app/home.html")

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    reponse = HttpResponse()
    reponse.writelines("<h1>Hello </h1>")
    reponse.write("This is app home")
    return reponse
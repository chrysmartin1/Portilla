from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def trial(request):
    my_dict = {'insert_me':" Much Joy"}
    return render(request,'camp2/trial.html',context=my_dict) #this context is linking what he hav in my_dict
def index(request):
    return render(request,'camp2/index.html')
def about(request):
    return render(request,'camp2/about.html')

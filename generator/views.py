from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    #return HttpResponse('Hello there Alok Rahul!!')
    return render(request, 'generator/home.html', {'password':'hsdu3edhs98'})
#<!--def eggs(request):
#    return HttpResponse('<h1>Eggs are so tasty, hence Sunday ho ya monday... Roz khao andey :D </h1>')/-->
def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%&*^'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))


    length = int(request.GET.get('length',12))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password':thepassword})

#This is to define the about request
def about(request):

    return render(request, 'generator/about.html')

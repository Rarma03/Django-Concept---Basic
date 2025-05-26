from django.http import HttpResponse
from django.shortcuts import render

def home(req):
    # return HttpResponse('Hey this is our (Home) response')
    return render(req, 'website/index.html')

def about(req):
    return HttpResponse('Hey this is our (About) response')

def contact(req):
    return HttpResponse('Hey this is our (Contact) response')


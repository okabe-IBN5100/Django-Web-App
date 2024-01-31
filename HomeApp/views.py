from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

import HomeApp

# Create your views here.
def index(request):
	
	dict = {'content':'Hello Django! '}

	return render(request, "HomeApp/index.html", dict)


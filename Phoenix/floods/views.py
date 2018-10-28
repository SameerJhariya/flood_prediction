# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import *

# Create your views here.

def home(request):
	return render(request, 'floods/home.html')

def floods(request):
	response = {}
	if request.method == "POST":
		word = Word()
		word.city = request.POST["city"]
		word.save()
		response["word"] = word
		if word.city == "Delhi":
			return redirect('/floods/data1')
		if word.city == "Mumbai":
			return redirect('/floods/data')
	return render(request, 'floods/floodsin.html', response)


def data(request):
	response = {}
	return render(request, 'floods/data.html', response)

def data1(request):
	return render(request, 'floods/data2.html')


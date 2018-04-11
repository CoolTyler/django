# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
  response = "placeholder to display all the surveys created"
  return HttpResponse(response)

def new(request):
  return HttpResponse("placeholder to display a new form to create a new survey")
    

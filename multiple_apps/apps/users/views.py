# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
  response = "placeholder to later display all the list of users"
  return HttpResponse(response)

def new(request):
  return HttpResponse("placeholder to display a new form to create a new user")
    
def create(request):
  return redirect('/users')

def show(request, user_id):
  return HttpResponse("placeholder to display user {}".format(user_id))

def edit(request, user_id):
  return HttpResponse("placeholder to edit user {}".format(user_id))
    
def delete(request, user_id):
  return redirect('/users')
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect



# Create your views here.
def index(request):
  response = "Hello, I am your first request!"
  return HttpResponse(response)

def new(request):
  return HttpResponse("placeholder to display a new form to create a new blog")
    
def create(request):
  return redirect('/blogs')

def show(request, blog_id):
  print blog_id
  return HttpResponse("placeholder to display blog {}".format(blog_id))

def edit(request, blog_id):
  return HttpResponse("placeholder to edit blog {}".format(blog_id))
    
def destroy(request, blog_id):
  return redirect('/blogs')
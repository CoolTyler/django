from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect



def index(request):
  response="Hi"
  return render(request, "survey_app/index.html")

def display_results(request):
  return render(request, "survey_app/results.html")

def process_form(request):
  try:
    request.session['tries']
  except KeyError:
    request.session['tries'] = 0
  request.session['name'] = request.POST['name']
  request.session['pet'] = request.POST['pet']
  request.session['body'] = request.POST['body']
  request.session['comment'] = request.POST['comment']
  request.session['tries'] += 1
  return redirect('/results')

# Create your views here.

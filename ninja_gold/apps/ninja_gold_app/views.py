# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
import random
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request): 
  try:
    request.session['total']
  except KeyError:
    request.session['total'] = 0
  return render(request, "ninja_gold_app/index.html")

def process(request, building_type):
  gold_amt = 0
  action = "gained"
  if building_type == "cave":
    gold_amt = random.randrange(5, 11)
  elif building_type == "farm":
    gold_amt = random.randrange(10, 21)
  elif building_type == "house":
    gold_amt = random.randrange(2, 6)
  else:
    gold_amt = random.randrange(-50, 51)
    if gold_amt < 0:
      action = "lost"
  # time_of = datetime.now().strftime("%Y/%m/%d %-I:%M%p")
  log = {
    "class": action,
    "message": "you {} {} gold from the {}".format(action, abs(gold_amt), building_type)
  }
  try:
    activity_log = request.session['logs']
  except KeyError:
    activity_log = []

  request.session['total'] += gold_amt
  activity_log.append(log)
  request.session['logs'] = activity_log
  return redirect('/')
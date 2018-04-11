# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import random
import string
# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
def random_word(n):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(n))
def index(request):
  # random = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(14)])
  try:
    request.session['tries']
  except KeyError:
      request.session['tries'] = 0
  return render(request, "rwg/index.html")

def generate(request):
  request.session['tries'] += 1
  request.session['word'] = random_word(14)
  return redirect('/')
  
def reset(request):
  del request.session['tries']
  del request.session['word']
  return redirect('/')

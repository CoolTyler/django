from __future__ import unicode_literals
from django.shortcuts import render, redirect
from datetime import datetime

# Create your views here.
def index(request):
  if 'words' not in request.session:
    request.session['words'] = []
  return render(request, "session_words_app/index.html")

def add_word(request):
  size = ''
  if 'big' in request.POST:
    size = 'big'
  color = ''
  if 'color' in request.POST:
    color = request.POST['color']
  date = datetime.now().strftime("%A, %b, %d")
  word = {
    'word': request.POST['word'],
    'color': color,
    'size': size,
    'created_at': date
  }
  temp = request.session['words']
  temp.append(word)
  request.session['words'] = temp
  return redirect('/')

def clear(request):
  del request.session['words']
  return redirect('/')
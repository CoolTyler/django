from __future__ import unicode_literals
import re
import bcrypt
from django.db import models

# Create your models here.

class UserManager(models.Manager):
  # validates the login data
  def validate_login(self, postData):
    results = {'status': True, 'errors': [], 'user' : None}
    users = self.filter(email = postData['email'])
    # checks if the email is in the database
    if len(users) < 1:
      results['status'] = False
      results['errors'].append('Not a registered email')
    else:
      if bcrypt.checkpw(postData['password'].encode(), users[0].password.encode()):
        results['user'] = users[0]
      else:
        results['status'] = False
    return results
  def creator(self, postData):
    user = self.create(first_name = postData['first_name'], last_name = postData['last_name'], email = postData['email'], password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt()))
    return user  
  def validate(self, postData):
    results = {'status': True, 'errors': []}
    if len(postData['first_name']) < 3:
      results['errors'].append('First name must be at least 2 characters')
      results['status'] = False
    if len(postData['last_name']) < 2:
      results['errors'].append('Last name must be at least 2 characters')
      results['status'] = False
    if not re.match("[^@]+@[^@]+\.[^@]+", postData['email']):
      results['errors'].append('Not a valid email address')
      results['status'] = False
    if len(postData['password']) < 8:
      results['errors'].append('Password must be at least 8 characters')
      results['status'] = False
    if postData['password'] != postData['c_password']:
      results['errors'].append('Passwords do not match')
      results['status'] = False
    if len(self.filter(email = postData['email'])) > 0:
      results['errors'].append('User already exists')
      results['status'] = False
    return results
  
    

class User(models.Model):
  first_name = models.CharField(max_length = 255)
  last_name = models.CharField(max_length = 255)
  email = models.CharField(max_length = 255)
  password  = models.CharField(max_length = 255)
  objects = UserManager()
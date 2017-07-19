from __future__ import unicode_literals
from django.db import models

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 1 or len(postData['last_name']) < 1:
            errors['name'] = 'First and last names cannot be blank!'
        
        if len(postData['email']) < 1:
            errors['email'] = 'Email cannot be blank!'
        elif not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Invalid email address!'
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BlogManager()
    def __repr__(self):
        return "<User object: {} {}>".format(self.first_name, self.last_name)
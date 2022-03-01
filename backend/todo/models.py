'''
Django imports a module models to help us build database models.
In our case, we created a todo model to store the title, memo, 
time of creation, time of completion and
user who created the todo
'''
from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    '''
     The properties have types like CharField, 
     TextField, DateTimeField
     Django provides many other model fields to support 
     common types like dates, integers, emails, etc
    '''
    title = models.CharField(max_length=100)
    memo = models.TextField(blank=True)

    #set to current time
    created = models.DateTimeField(auto_now_add=True) 
    completed = models.BooleanField(default=False)

    #user who posted this
    user = models.ForeignKey(User, on_delete=models.CASCADE) 

    def __str__(self):
        #  include a __str__ method so that 
        # the title of a todo will display in the admin later on
        return self.title

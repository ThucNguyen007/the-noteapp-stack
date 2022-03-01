from rest_framework import serializers
from todo.models import Todo

# ModelSerializer provides an API to create serializers from your models
class TodoSerializer(serializers.ModelSerializer):
    # auto populated by app. Users cannot be edited when it is fixed
    created = serializers.ReadOnlyField()   
    completed = serializers.ReadOnlyField()  
    '''
    Specifying our database model Todo and the fields to expose i.e.
    ['id','title','memo','created','completed']
    Django REST Framework then magically transforms model data into
    JSON, exposing these fields Todo model
    Fields not specified here will not be exposed in the API. 
    'id' is created automatically by Django so don't have to define it 
    in Todo model. But using it in the API
    '''
    class Meta:
        model = Todo
        fields = ['id','title','memo','created','completed']

'''
The TodoToggleCompleteSerializer doesn't receive and update 
any of the fields values from the endpoint
set the fields to read only by specifying them in the Meta shortcut option
read_only_fields. read_only_fields allows us to specify multiple fields as read-only.
'''
class TodoToggleCompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id'] 
        read_only_fields = ['title','memo','created','completed']


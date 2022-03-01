# import DRF’s generics class of views
from rest_framework import generics, permissions
from .serializers import TodoSerializer, TodoToggleCompleteSerializer
from todo.models import Todo
from django.db import IntegrityError
from django.contrib.auth.models import User
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate

'''
ListCreateAPIView is a built-in generic class which creates a
read-only for model instances for the API end point
'''
class TodoListCreate(generics.ListCreateAPIView):
    # requires two mandatory attributes, 
    # serializer_class and queryset.
    # We specify TodoSerializer which we have earlier implemented
    serializer_class = TodoSerializer
    # specifying  that only authenticated and registered users 
    # have permission to call this API
    # Unauthenticated users are not allowed to access it
    permission_classes = [permissions.IsAuthenticated]
    '''
    get_queryset returns the queryset of todo objects for the view 
    specifying the query set as all todos which match the user. 
    ordering the todos by the created date shown the latest todo first
    '''
    def get_queryset(self):
        user = self.request.user        
        return Todo.objects.filter(user=user).order_by('-created')
    '''
    acts as a hook which is called before the instance is created in the database
    Thus, specifying the user of the todo as the request’s user before creation in the database
    '''
    def perform_create(self, serializer):
        #serializer holds a django model
        serializer.save(user=self.request.user) 

class TodoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # user can only update, delete own posts
        return Todo.objects.filter(user=user)
'''
It toggles a todo from incomplete to complete and vice-versa
It extends the UpdateAPIView used for update-only endpoints 
for a single model instance
'''
class TodoToggleComplete(generics.UpdateAPIView):
    serializer_class = TodoToggleCompleteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user)
    '''
    perform update called before the update happens
    Invert the todo completed boolean value
    If it is false, set to true and otherwise.
    '''
    def perform_update(self,serializer):
        serializer.instance.completed=not(serializer.instance.completed)
        serializer.save()

# cross site request forgery
#  the POST request is coming from a different domain 
# (the frontend domain) and will not have the token
# required to pass the CSRF checks
@csrf_exempt
def signup(request):
    # the sign up form in the front end 
    # will use POST request for form submissions
    if request.method == 'POST':
        try:
            # JSONParse().parse to parse the JSON request content 
            # and return a dictionary of data.
            data = JSONParser().parse(request)
            user = User.objects.create_user(
                username=data['username'], 
                password=data['password'])
            # save the user object to the database
            user.save()
            # create the token object
            token = Token.objects.create(user=user)
            # If all goes well, return a JSonResponse object 
            # with a dictionary containing the token, 
            # and status code of 201 indicating successful creation
            return JsonResponse({'token':str(token)}, status=201) 
        except IntegrityError:
            return JsonResponse(
                {'error':'username taken. choose another username'}, 
                status=400)

@csrf_exempt
def login(request):
    if request.method == 'POST':        
        data = JSONParser().parse(request)
        user = authenticate(
            request,
            username=data['username'],
            password=data['password'])
        '''
        If no user is found, return a JsonResponse object 
        with a dictionary containing an error message and status code
        of 400 indicating that the request cannot be fulfilled.
        '''
        if user is None:
            return JsonResponse(
                {'error':'unable to login. check username and password'}, 
                status=400)
        else: # if found the authentication, return user token
            try:
                token = Token.objects.get(user=user)
            except: # if token not in db, create a new one
                token = Token.objects.create(user=user)
            return JsonResponse({'token':str(token)}, status=201)
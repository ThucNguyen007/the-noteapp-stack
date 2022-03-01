from django.urls import path
from . import views

urlpatterns = [
    # views.TodoList is an instance of a class-based generic view
    # to similarly send customized serialized data
    # to the API endpoints
    path('todos/', views.TodoListCreate.as_view()),
    # to retrieve, update or delete an individual todo
    path('todos/<int:pk>', views.TodoRetrieveUpdateDestroy.as_view()),
    # if a request is sent to localhost:8000/api/todos/2/complete, 
    # the todo with id '2' will be marked as complete
    path('todos/<int:pk>/complete', views.TodoToggleComplete.as_view()),
    path('signup/', views.signup),
    # create a url for them to login and retrieve a token
    path('login/', views.login),
]

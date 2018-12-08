from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name = 'home'),
    path('author/<name>',getauthor, name = 'author'),
    path('article/<int:id>', getsingle, name = 'single_post'),
    path('topic/<name>', getTopic, name = 'topic')
    
    
    
    
]
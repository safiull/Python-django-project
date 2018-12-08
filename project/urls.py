from django.urls import path
from .views import *


urlpatterns = [
    path('dirmitory/', dirmitory, name = 'dirmitory'),
    path('name/', name, name = 'name'),
    path('details/<int:id>', details, name = 'details')

]
from django.urls import path
from . import views
urlpatterns =[
    path('create-case/', views.create_case, name='create_case'),
    path('get-all-case/', views.get_all_cases, name='all_cases'),
]
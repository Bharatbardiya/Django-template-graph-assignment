from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='landing-page'),
    path('question/<questionNo>', views.question_solution, name='school-graph')
    
]
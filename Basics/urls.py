from django.urls import path
from Basics import views

urlpatterns = [
    path('Sum/',views.Sum,name="Sum"),
    path('Large/',views.Large,name="Large"),
    path('Calc/',views.Calc,name="Calc"),
]
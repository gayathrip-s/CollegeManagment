from django.urls import path
from Guest import views
app_name="Guest"

urlpatterns = [
    path('UserReg/',views.UserReg,name="UserReg"),
    path('Login/',views.Login,name="Login"),
    path('Ajaxplace/',views.Ajaxplace,name="Ajaxplace"),
    
]
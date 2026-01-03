from django.urls import path
from User import views
app_name="User"

urlpatterns = [
    path('Homepage/',views.Homepage,name="Homepage"),
    path('Myprofile/',views.Myprofile,name="Myprofile"),
    path('Editprofile/',views.Editprofile,name="Editprofile"),
    path('Changepass/',views.Changepass,name="Changepass"),
   
]
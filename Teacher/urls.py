from django.urls import path
from Teacher import views
app_name="Teacher"

urlpatterns = [
   path('Homepage/',views.Homepage,name="Homepage"),
   path('Myprofile/',views.Myprofile,name="Myprofile"),
   path('Editprofile/',views.Editprofile,name="Editprofile"),
   path('Changepass/',views.Changepass,name="Changepass"),
   path('Addstudent/',views.Addstudent,name="Addstudent"),
   path('delstudent/<int:did>/',views.delstudent,name="delstudent"),
   path('Addnotes/',views.Addnotes,name="Addnotes"),
   path('delnotes/<int:did>/',views.delnotes,name="delnotes"),
   path('Ajaxassignsubject/',views.Ajaxassignsubject,name="Ajaxassignsubject"),
   path('Assignment/',views.Assignment,name="Assignment"),
   path('delassignment/<int:did>/',views.delassignment,name="delassignment"),
   path('Viewuploads/<int:aid>/',views.Viewuploads,name="Viewuploads"),
   path('Addmark/<int:aid>/',views.Addmark,name="Addmark"),
]
from django.db import models
from Admin.models import *
# Create your models here.
class tbl_student(models.Model):
    student_name=models.CharField(max_length=50)
    student_email=models.CharField(max_length=50)
    student_contact=models.CharField(max_length=50)
    student_address=models.CharField(max_length=50)
    student_photo=models.FileField(upload_to="Assets/StudentDocs/")
    student_gender=models.CharField(max_length=50)
    student_dob=models.CharField(max_length=50)
    student_password=models.CharField(max_length=50)
    assignclass=models.ForeignKey(tbl_assignclass,on_delete=models.CASCADE)

class tbl_notes(models.Model):
    notes_file=models.FileField(upload_to="Assets/Notes/")
    notes_content=models.CharField(max_length=50)
    subject=models.ForeignKey(tbl_subject,on_delete=models.CASCADE)
    teacher=models.ForeignKey(tbl_teacher,on_delete=models.CASCADE)

class tbl_assignment(models.Model):
    assignment_title=models.CharField(max_length=100)
    assignment_file=models.FileField(upload_to="Assets/Assignments/")
    assignment_duedate=models.DateField()
    assignment_date=models.DateField(auto_now_add=True)
    assignment_status = models.IntegerField(default=0)
    subject=models.ForeignKey(tbl_subject,on_delete=models.CASCADE)
    teacher=models.ForeignKey(tbl_teacher,on_delete=models.CASCADE)

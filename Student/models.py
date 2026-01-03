from django.db import models
from Teacher.models import *
# Create your models here.
class tbl_complaint(models.Model):
    comp_title = models.CharField(max_length=200)
    com_content =  models.TextField()
    com_date =  models.DateField(auto_now_add=True)
    com_status = models.IntegerField(default=0)
    com_reply = models.TextField()
    student= models.ForeignKey(tbl_student,on_delete=models.CASCADE)

class tbl_assignmentbody(models.Model):
    ass_date = models.DateField(auto_now_add=True)
    ass_status = models.IntegerField(default=0)
    ass_score = models.CharField(max_length=200)
    ass_file = models.FileField(upload_to="Assets/Assignment/Files/")
    student =  models.ForeignKey(tbl_student,on_delete=models.CASCADE)
    assignment = models.ForeignKey(tbl_assignment,on_delete=models.CASCADE)

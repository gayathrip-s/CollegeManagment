from django.db import models

# Create your models here.
class tbl_district(models.Model):
    district_name = models.CharField(max_length=50)

class tbl_admin(models.Model):
    admin_name=models.CharField(max_length=15)
    admin_email=models.CharField(max_length=30)
    admin_password=models.CharField(max_length=10)

class tbl_category(models.Model):
    category_name=models.CharField(max_length=50)

class tbl_place(models.Model):
    place_name=models.CharField(max_length=50)
    district = models.ForeignKey(tbl_district,on_delete=models.CASCADE)

class tbl_subcategory(models.Model):
    subcategory_name=models.CharField(max_length=50)
    category = models.ForeignKey(tbl_category,on_delete=models.CASCADE)

class tbl_department(models.Model):
    department_name=models.CharField(max_length=50)

class tbl_semester(models.Model):
    semester_name=models.CharField(max_length=50)

class tbl_academicyear(models.Model):
    academicyear_name=models.CharField(max_length=50)

class tbl_course(models.Model):
    course_name=models.CharField(max_length=60)
    department = models.ForeignKey(tbl_department,on_delete=models.CASCADE)

class tbl_subject(models.Model):
    subject_name=models.CharField(max_length=100)
    course = models.ForeignKey(tbl_course,on_delete=models.CASCADE)
    semester = models.ForeignKey(tbl_semester,on_delete=models.CASCADE)

class tbl_class(models.Model):
    class_name=models.CharField(max_length=60)
    course = models.ForeignKey(tbl_course,on_delete=models.CASCADE)

class tbl_teacher(models.Model):
    teacher_name=models.CharField(max_length=50)
    teacher_email=models.CharField(max_length=50)
    teacher_contact=models.CharField(max_length=50)
    teacher_role=models.CharField(max_length=50)
    teacher_gender=models.CharField(max_length=50)
    teacher_photo=models.FileField(upload_to="Assets/TeacherDocs/")
    teacher_password=models.CharField(max_length=50)
    department = models.ForeignKey(tbl_department,on_delete=models.CASCADE)

class tbl_assignclass(models.Model):
    Class = models.ForeignKey(tbl_class,on_delete=models.CASCADE)
    teacher = models.ForeignKey(tbl_teacher,on_delete=models.CASCADE)
    academicyear = models.ForeignKey(tbl_academicyear,on_delete=models.CASCADE)

class tbl_assignsubject(models.Model):
    teacher = models.ForeignKey(tbl_teacher,on_delete=models.CASCADE)
    academicyear = models.ForeignKey(tbl_academicyear,on_delete=models.CASCADE)
    subject=models.ForeignKey(tbl_subject,on_delete=models.CASCADE)





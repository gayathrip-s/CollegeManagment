from django.shortcuts import render
from Admin.models import *
from Teacher.models import *
from Student.models import *

# Create your views here.
def Homepage(request):
    return render(request,"Teacher/Homepage.html")

def Myprofile(request):
  teacherdata = tbl_teacher.objects.get(id=request.session['tid'])
  return render(request,"Teacher/Myprofile.html",{'teacher':teacherdata})

def Editprofile(request):
  teacherdata = tbl_teacher.objects.get(id=request.session['tid'])
  if request.method == "POST":
    name=request.POST.get("txt_name")
    email=request.POST.get("txt_email")
    contact=request.POST.get("txt_contact")

    teacherdata.teacher_name = name
    teacherdata.teacher_email= email
    teacherdata.teacher_contact= contact
    teacherdata.save()
    return render(request,"Teacher/Editprofile.html",{'msg':"Data Updated..."})
  else:
    return render(request,"Teacher/Editprofile.html",{'teacher':teacherdata})

def Changepass(request):
  teacherdata = tbl_teacher.objects.get(id=request.session['tid'])
  dbpass=teacherdata.teacher_password
  if request.method == "POST":
    password=request.POST.get("txt_password")
    newpassword=request.POST.get("txt_newpassword")
    repassword=request.POST.get("txt_repassword")  
    if dbpass==password:
      if newpassword==repassword:
        teacherdata.teacher_password = newpassword
        teacherdata.save()
        return render(request,"Teacher/Changepass.html",{'msg':"Password changed..."})
      else:
        return render(request,"Teacher/Changepass.html",{'msg':"Password does not match..."})
    else:
      return render(request,"Teacher/Changepass.html",{'msg':"Invalid Old password..."})
  else:
    return render(request,"Teacher/Changepass.html")

def Addstudent(request):
    teacher=tbl_teacher.objects.get(id=request.session['tid'])
    assignclid = tbl_assignclass.objects.filter(teacher=teacher).last()
    studentdata=tbl_student.objects.filter(assignclass=assignclid)

    if request.method=="POST":
        name=request.POST.get("txt_name")
        email=request.POST.get("txt_email")
        contact=request.POST.get("txt_contact")
        address=request.POST.get("txt_address")
        photo= request.FILES.get("file_photo")
        gender=request.POST.get("txt_gender")
        dob=request.POST.get("txt_date")
        password=request.POST.get("txt_password")
        tbl_student.objects.create(student_name=name,student_email=email,student_contact=contact,student_address=address,
        student_photo=photo,student_gender=gender,student_dob=dob,student_password=password,assignclass=assignclid)
        return render(request,"Teacher/Addstudent.html",{'msg':"Data Inserted..."})
    else:
        return render(request,"Teacher/Addstudent.html",{'studentdata':studentdata})

def delstudent(request,did):
    tbl_student.objects.get(id=did).delete()
    return render(request,"Teacher/Addstudent.html",{'msg':"Data Deleted..."})

def Addnotes(request):
  teacher =  tbl_teacher.objects.get(id=request.session['tid'])
  department = teacher.department
  coursedata=tbl_course.objects.filter(department=department)
  semesterdata=tbl_semester.objects.all()
  addnotesdata=tbl_notes.objects.filter(teacher=teacher)
  if request.method=="POST":
    file = request.FILES.get("file_note")
    content = request.POST.get("txt_content")
    subject = tbl_subject.objects.get(id=request.POST.get("sel_subject"))
    tbl_notes.objects.create(notes_file=file,notes_content=content,teacher=teacher,subject=subject)
    return render(request,"Teacher/Addnotes.html",{'msg':"Data Inserted..."})
  else:
    return render(request,"Teacher/Addnotes.html",{'coursedata':coursedata,'semesterdata':semesterdata,'addnotesdata':addnotesdata})

def delnotes(request,did):
    tbl_notes.objects.get(id=did).delete()
    return render(request,"Teacher/Addnotes.html",{'msg':"Data Deleted..."})

 

def Ajaxassignsubject(request):
  courseId = request.GET.get("courseId")
  semId = request.GET.get("semId")
  teacher = tbl_teacher.objects.get(id=request.session['tid'])
  subjectdata = tbl_assignsubject.objects.filter(subject__course=courseId,subject__semester=semId,teacher=teacher)
  return render(request,"Teacher/AjaxAssignSubject.html",{'subjectdata':subjectdata})


def Assignment(request):
  teacher =  tbl_teacher.objects.get(id=request.session['tid'])
  department = teacher.department
  coursedata=tbl_course.objects.filter(department=department)
  semesterdata=tbl_semester.objects.all()
  assignmentdata=tbl_assignment.objects.filter(teacher=teacher)
  if request.method=="POST":
    title = request.POST.get("txt_title")
    file = request.FILES.get("file_assignment")
    duedate = request.POST.get("txt_date")
    subject = tbl_subject.objects.get(id=request.POST.get("sel_subject"))
    tbl_assignment.objects.create(assignment_title=title,assignment_file=file,assignment_duedate=duedate,teacher=teacher,subject=subject)
    return render(request,"Teacher/Assignment.html",{'msg':"Data Inserted..."})
  else:
    return render(request,"Teacher/Assignment.html",{'coursedata':coursedata,'semesterdata':semesterdata,'assignmentdata':assignmentdata})
  

def delassignment(request,did):
    tbl_notes.objects.get(id=did).delete()
    return render(request,"Teacher/Assignment.html",{'msg':"Data Deleted..."})

def Viewuploads(request,aid):
   submitdata=tbl_assignmentbody.objects.filter(assignment=aid)
   return render(request,"Teacher/Viewuploads.html",{'submitdata':submitdata,})

def Addmark(request,aid):
    subassignment=tbl_assignmentbody.objects.get(id=aid)
    if request.method == "POST":
      mark=request.POST.get("txt_mark")
      subassignment.ass_score=mark
      subassignment.ass_status=1
      subassignment.save()
      return render(request,"Teacher/Addmark.html",{'msg':"Score Updated...",'aid':aid})
    else:
      return render(request,"Teacher/Addmark.html")
     
      

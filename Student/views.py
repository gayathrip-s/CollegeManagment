from django.shortcuts import render
from Teacher.models import *
from Admin.models import *
from Student.models import *

# Create your views here.
def Homepage(request):
 
  return render(request,"Student/Homepage.html")

def Myprofile(request):
  studentdata = tbl_student.objects.get(id=request.session['sid'])
  return render(request,"Student/Myprofile.html",{'student':studentdata})

def Editprofile(request):
  studentdata = tbl_student.objects.get(id=request.session['sid'])
  if request.method == "POST":
    name=request.POST.get("txt_name")
    email=request.POST.get("txt_email")
    contact=request.POST.get("txt_contact")
    address=request.POST.get("txt_address")
        
    studentdata.student_name = name
    studentdata.student_email= email
    studentdata.student_contact= contact
    studentdata.student_address= address
    studentdata.save()
    
    return render(request,"Student/EditProfile.html",{'msg':"Data Updated..."})
  else:
    return render(request,"Student/EditProfile.html",{'student':studentdata})
 

def Changepass(request):
  studentdata = tbl_student.objects.get(id=request.session['sid'])
  dbpass=studentdata.student_password
  if request.method == "POST":
    password=request.POST.get("txt_password")
    newpassword=request.POST.get("txt_newpassword")
    repassword=request.POST.get("txt_repassword")  
    if dbpass==password:
      if newpassword==repassword:
        studentdata.student_password = newpassword
        studentdata.save()
        return render(request,"Student/Changepass.html",{'msg':"Password changed..."})
      else:
        return render(request,"Student/Changepass.html",{'msg':"Password does not match..."})
    else:
      return render(request,"Student/Changepass.html",{'msg':"Invalid Old password..."})
  else:
    return render(request,"Student/Changepass.html")

def Viewnotes(request):
  semesterdata = tbl_semester.objects.all()
  return render(request,"Student/Viewnotes.html",{'semesterdata':semesterdata})

def AjaxSubject(request):
  semid = request.GET.get("semid")
  studentdata = tbl_student.objects.get(id=request.session['sid'])
  courseId = studentdata.assignclass.Class.course
  subjectdata=tbl_subject.objects.filter(course=courseId,semester=semid)
  return render(request,"Student/AjaxSubject.html",{'subjectdata':subjectdata})

def Ajaxnotes(request):
  subid = request.GET.get("subid")
  notedata = tbl_notes.objects.filter(subject=subid)
  return render(request,"Student/Ajaxnotes.html",{'notedata':notedata})

def Viewassignment(request):
  assignmentdata= tbl_assignment.objects.all()
  return render(request,"Student/Viewassignment.html",{'assignmentdata':assignmentdata})

def Submitassignment(request,aid):
  assignment=tbl_assignment.objects.get(id=aid)
  studentdata = tbl_student.objects.get(id=request.session['sid'])
  submitdata = tbl_assignmentbody.objects.filter(student=studentdata,assignment=assignment)
  if request.method =="POST":
    ass=request.FILES.get("file_submit")
    tbl_assignmentbody.objects.create(ass_file=ass, student=studentdata,assignment=assignment)
    return render(request,"Student/Submitassignment.html",{'msg':"Data Inserted...",'aid':aid})
  else:
    return render(request,"Student/Submitassignment.html",{'submitdata':submitdata,'aid':aid})

    
def delassign(request,did,aid):
    tbl_assignmentbody.objects.get(id=did).delete()
    return render(request,"Student/Submitassignment.html",{'msg':"Data Deleted...",'aid':aid})

def Myassignments(request):
  submitdata=tbl_assignmentbody.objects.filter(student=request.session['sid'])
  return render(request,"Student/Myassignments.html",{'submitdata':submitdata})

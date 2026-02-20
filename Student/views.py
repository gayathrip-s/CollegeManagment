from django.shortcuts import render
from Teacher.models import *
from Admin.models import *
from Student.models import *
from django.db.models import Count, Q
from datetime import date
from django.utils import timezone


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

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

HOURS = [
    ("1", "10:00 - 10:55"),
    ("2", "10:55 - 11:50"),
    ("3", "12:05 - 01:00"),
    ("4", "02:00 - 03:00"),
    ("5", "03:00 - 04:00"),
]



def ViewTimeTable(request):
    student = tbl_student.objects.get(id=request.session['sid'])
    assignclass =student.assignclass
    course = assignclass.Class.course
    current_semester = tbl_classsem.objects.order_by('assignclass_id').last()
    academicyear = tbl_academicyear.objects.order_by('-id').first()

    timetable = tbl_timetable.objects.none()

    if current_semester and academicyear:
        timetable = tbl_timetable.objects.filter(
            course=course,
            semester=current_semester.semester,
            academicyear=academicyear
        )

    return render(request, "Student/ViewTimeTable.html", {
        "student": student,
        "timetable": timetable,
        "days": DAYS,
        "hours": HOURS,
        "semester": current_semester,
        "course": course,
        "academicyear": academicyear
    })


def Complaint(request):
    studentdata = tbl_student.objects.get(id=request.session['sid'])
    complaintdata = tbl_complaint.objects.filter(student=studentdata)
    if request.method == "POST":
        title = request.POST.get("txt_title")
        content = request.POST.get("txt_content")
        tbl_complaint.objects.create(comp_title=title,com_content=content,
            student=studentdata)
        return render(request, "Student/Complaint.html", {'msg': "Complaint Submitted..."})
    else:
        return render(request, "Student/Complaint.html",{'complaintdata':complaintdata})

def delcomplaint(request,did):
    tbl_complaint.objects.get(id=did).delete()
    return render(request,"Student/Complaint.html",{'msg':"Data Deleted..."})
def viewattendance(request):
    studentdata = tbl_student.objects.get(id=request.session['sid'])
    semesterdata = tbl_semester.objects.all()

    today = timezone.now().date()

    # ✅ Get Last Inserted Class Semester
    last_classsem = tbl_classsem.objects.all().order_by('-id').first()

    current_semester = None
    if last_classsem:
        current_semester = last_classsem.semester  # assuming FK name is semester

    attendancedata = None
    overall_percentage = 0

    if request.method == "POST":

        selected_semester = request.POST.get("sel_semester")
        from_date = request.POST.get("from_date")
        to_date = request.POST.get("to_date")

        attendancedata = tbl_attendance.objects.filter(student=studentdata)

        if selected_semester:
            attendancedata = attendancedata.filter(semester_id=selected_semester)

        if from_date and to_date:
            attendancedata = attendancedata.filter(date__range=[from_date, to_date])

    else:
        # ✅ Default: Today's attendance of last inserted semester
        if current_semester:
            attendancedata = tbl_attendance.objects.filter(
                student=studentdata,
                semester=current_semester,
                date=today
            )

    # ✅ Overall attendance of current semester
    if current_semester:
        semester_attendance = tbl_attendance.objects.filter(
            student=studentdata,
            semester=current_semester
        )

        total = semester_attendance.count()
        present = semester_attendance.filter(status=1).count()

        if total > 0:
            overall_percentage = (present / total) * 100

    return render(request, "Student/ViewAttendance.html", {
        "semesterdata": semesterdata,
        "attendancedata": attendancedata,
        "selected_semester": current_semester.id if current_semester else None,
        "today": today,
        "overall_percentage": overall_percentage
    })

def leaveapplication(request):
    studentdata = tbl_student.objects.get(id=request.session['sid'])
    leavedata = tbl_leave.objects.filter(student=studentdata)
    if request.method == "POST":
        title = request.POST.get("txt_title")
        reason = request.POST.get("txt_reason")
        fromdate = request.POST.get("txt_fromdate")
        todate = request.POST.get("txt_todate")
        tbl_leave.objects.create(leave_title=title,leave_reason=reason,
            leave_fromdate=fromdate,leave_todate=todate,
            student=studentdata)
        return render(request, "Student/Leave.html", {'msg': "Leave Application Submitted..."})
    else:
        return render(request, "Student/Leave.html",{'leavedata':leavedata})
   
def delleave(request,did):
    tbl_leave.objects.get(id=did).delete()
    return render(request,"Student/Leave.html",{'msg':"Data Deleted..."})

def dutyleave(request):
   studentdata = tbl_student.objects.get(id=request.session['sid'])
   dutyleavedata = tbl_dutyleave.objects.filter(student=studentdata)
   purposedata = tbl_purpose.objects.all()
   if request.method == "POST":
      purposeid=tbl_purpose.objects.get(id=request.POST.get("sel_purpose"))
      reason = request.POST.get("txt_reason")
      hour = request.POST.get("txt_hour")
      fromdate = request.POST.get("txt_fromdate")
      todate = request.POST.get("txt_todate")
      tbl_dutyleave.objects.create(dutyleave_reason=reason,dutyleave_hour=hour,dutyleave_fromdate=fromdate,dutyleave_todate=todate,
          student=studentdata,purpose=purposeid)
      return render(request, "Student/Dutyleave.html", {'msg': "Duty Leave Submitted..."})
   else:
      return render(request, "Student/Dutyleave.html",{'dutyleavedata':dutyleavedata,'purposedata':purposedata})
          
def deldutyleave(request,did):
    tbl_dutyleave.objects.get(id=did).delete()
    return render(request,"Student/Dutyleave.html",{'msg':"Data Deleted..."})
         
         
    
   
  
  
    
   
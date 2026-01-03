from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import *
from Teacher.models import *

# Create your views here.
def UserReg(request):
    
    districtdata=tbl_district.objects.all()
    if request.method == "POST":
        name=request.POST.get("txt_name")
        email=request.POST.get("txt_mail")
        contact=request.POST.get("txt_contact")
        address=request.POST.get("txt_address")
        photo= request.FILES.get("file_photo")
        password=request.POST.get("txt_password")
        place=tbl_place.objects.get(id=request.POST.get("sel_place"))
        tbl_user.objects.create(user_name=name,user_email=email,user_contact=contact,user_address=address,user_photo=photo,
        user_password=password,place=place)
        return render(request,"Guest/UserRegistration.html",{'msg':"Data Inserted..."})
    else:
        return render(request,"Guest/UserRegistration.html",{'districtdata':districtdata})
def Ajaxplace(request):
    place=tbl_place.objects.filter(district=request.GET.get('disid'))
    return render(request,"Guest/Ajaxplace.html",{'data':place})

def Login(request):
    if request.method == "POST":
    
        email=request.POST.get("txt_mail")
        password=request.POST.get("txt_password")

        usercount = tbl_user.objects.filter(user_email=email,user_password=password).count()
        admincount = tbl_admin.objects.filter(admin_email=email,admin_password=password).count()
        teachercount = tbl_teacher.objects.filter(teacher_email=email,teacher_password=password).count()
        studentcount = tbl_student.objects.filter(student_email=email,student_password=password).count()
        if usercount > 0:
            user = tbl_user.objects.get(user_email=email,user_password=password)
            request.session['uid'] = user.id
            return redirect("User:Homepage")
        elif admincount > 0:
            admin=tbl_admin.objects.get(admin_email=email,admin_password=password)
            request.session['aid'] = admin.id
            return redirect("Admin:Homepage")
        elif teachercount > 0:
            teacher=tbl_teacher.objects.get(teacher_email=email,teacher_password=password)
            request.session['tid'] = teacher.id
            return redirect("Teacher:Homepage")
        elif studentcount > 0:
            student=tbl_student.objects.get(student_email=email,student_password=password)
            request.session['sid'] = student.id
            return redirect("Student:Homepage")
        else:
            return render(request,"Guest/Login.html",{"msg":"Invalid Email or Password"})
    else:
        return render(request,"Guest/Login.html")


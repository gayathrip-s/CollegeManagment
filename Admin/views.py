from django.shortcuts import render
from Admin.models import *

# Create your views here.

def District(request):
    districtdata = tbl_district.objects.all()
    if request.method=="POST":
        name=request.POST.get("txt_district")
        tbl_district.objects.create(district_name=name)
        #return redirect("Admin:District")
        return render(request,"Admin/District.html",{'msg':"Data Inserted..."})    
    else: 
        return render(request,"Admin/District.html",{'districtdata':districtdata})

def deldistrict(request,did):
    tbl_district.objects.get(id=did).delete()
    return render(request,"Admin/District.html",{'msg':"Data Deleted..."})    

def editdistrict(request,eid):
    editdata = tbl_district.objects.get(id=eid)
    districtdata = tbl_district.objects.all()
    if request.method == "POST":
        name=request.POST.get("txt_district")
        editdata.district_name = name
        editdata.save()
        return render(request,"Admin/District.html",{'msg':"Data Updated..."})    
    else:
        return render(request,"Admin/District.html",{'editdata':editdata,'districtdata':districtdata})

def AdminReg(request):
    admindata=tbl_admin.objects.all()
    if request.method=="POST":
        name=request.POST.get("txt_name")
        email=request.POST.get("txt_mail")
        password=request.POST.get("txt_password")
        tbl_admin.objects.create(admin_name=name,admin_email=email,admin_password=password)
        return render(request,"Admin/AdminRegistration.html",{'msg':"Data Inserted..."})    
    else: 
        return render(request,"Admin/AdminRegistration.html",{'admindata':admindata})

def deladmin(request,did):
    tbl_admin.objects.get(id=did).delete()
    return render(request,"Admin/AdminRegistration.html",{'msg':"Data Deleted"})

def editadmin(request,eid):
    editdata=tbl_admin.objects.get(id=eid)
    admindata=tbl_admin.objects.all()
    if request.method == "POST":
        name=request.POST.get("txt_name")
        editdata.admin_name=name
        email=request.POST.get("txt_mail")
        editdata.admin_email=email
        password=request.POST.get("txt_password")
        editdata.admin_password=password
        editdata.save()
        return render(request,"Admin/AdminRegistration.html",{'msg':"Data Updated..."})
    else:
        return render(request,"Admin/AdminRegistration.html",{'editdata':editdata,'admindata':admindata})

def Category(request):
    categorydata=tbl_category.objects.all()
    if request.method=="POST":
        name=request.POST.get("txt_category")
        tbl_category.objects.create(category_name=name)
        return render(request,"Admin/Category.html",{'msg':"Data Inserted..."})
    else:
        return render(request,"Admin/Category.html",{'categorydata':categorydata})

def delcategory(request,did):
    tbl_category.objects.get(id=did).delete()
    return render(request,"Admin/Category.html",{'msg':"Data Deleted..."})

def editcategory(request,eid):
    editdata=tbl_category.objects.get(id=eid)
    categorydata=tbl_category.objects.all()
    if request.method == "POST":
        name=request.POST.get("txt_category")
        editdata.category_name=name
        editdata.save()
        return render(request,"Admin/Category.html",{'msg':"Data Updated..."})
    else:
        return render(request,"Admin/Category.html",{'editdata':editdata,'categorydata':categorydata})
    

def Place(request):
    placedata=tbl_place.objects.all()
    districtdata=tbl_district.objects.all()
    if request.method=="POST":
        place=request.POST.get("txt_place")
        district=tbl_district.objects.get(id=request.POST.get("sel_district"))
        tbl_place.objects.create(place_name=place,district=district)
        return render(request,"Admin/Place.html",{'msg':"Data Inserted..."})
    else:
        return render(request,"Admin/Place.html",{'districtdata':districtdata,'placedata':placedata})

def deleteplace(request,did):
    tbl_place.objects.get(id=did).delete()
    return render(request,"Admin/Place.html",{'msg':"Data Deleted..."})

def editplace(request,eid):
    editdata=tbl_place.objects.get(id=eid)
    placedata=tbl_place.objects.all()
    districtdata=tbl_district.objects.all()
    if request.method == "POST":
        name=request.POST.get("txt_place")
        district=tbl_district.objects.get(id=request.POST.get("sel_district"))
        editdata.place_name=name
        editdata.district = district
        editdata.save()
        return render(request,"Admin/Place.html",{'msg':"Data Updated..."})
    else:
        return render(request,"Admin/Place.html",{'editdata':editdata,'placedata':placedata,'districtdata':districtdata})


def Subcategory(request):
    subcatdata=tbl_subcategory.objects.all()
    categorydata=tbl_category.objects.all()
    if request.method=="POST":
        subcategory=request.POST.get("txt_subcategory")
        category=tbl_category.objects.get(id=request.POST.get("sel_category"))
        tbl_subcategory.objects.create(subcategory_name=subcategory,category=category)
        return render(request,"Admin/Subcategory.html",{'msg':"Data Inserted..."})
    else:
        return render(request,"Admin/Subcategory.html",{'categorydata':categorydata,'subcatdata':subcatdata})

def delsubcategory(request,did):
    tbl_subcategory.objects.get(id=did).delete()
    return render(request,"Admin/Subcategory.html",{'msg':"Data Deleted..."})

def editsubcategory(request,eid):
    editdata=tbl_subcategory.objects.get(id=eid)
    subcatdata=tbl_subcategory.objects.all()
    categorydata=tbl_category.objects.all()
    if request.method == "POST":
        name=request.POST.get("txt_subcategory")
        editdata.subcategory_name=name
        editdata.save()
        return render(request,"Admin/Subcategory.html",{'msg':"Data Updated..."})
    else:
        return render(request,"Admin/Subcategory.html",{'editdata':editdata,'subcatdata':subcatdata,'categorydata':categorydata})


def Department(request):
    departmentdata = tbl_department.objects.all()
    if request.method=="POST":
        department=request.POST.get("txt_department")
        tbl_department.objects.create(department_name=department)
        return render(request,"Admin/Department.html",{'msg':"Data Inserted..."})
    else:
        return render(request,"Admin/Department.html",{'departmentdata':departmentdata})

def deldepartment(request,did):
    tbl_department.objects.get(id=did).delete()
    return render(request,"Admin/Department.html",{'msg':"Data Deleted..."})  

def Semester(request):
    semesterdata=tbl_semester.objects.all()
    if request.method=="POST":
        semester=request.POST.get("txt_semester")
        tbl_semester.objects.create(semester_name=semester)
        return render(request,"Admin/Semester.html",{'msg':"Data Inserted..."})
    else:
        return render(request,"Admin/Semester.html",{'semesterdata':semesterdata})

def delsemester(request,did):
    tbl_semester.objects.get(id=did).delete()
    return render(request,"Admin/Semester.html",{'msg':"Data Deleted..."})

def Academicyear(request):
    academicyeardata=tbl_academicyear.objects.all()
    if request.method=="POST":
        year=request.POST.get("txt_academicyear")
        tbl_academicyear.objects.create(academicyear_name=year)
        return render(request,"Admin/Academicyear.html",{'msg':"Data Inserted..."})
    else:
        return render(request,"Admin/Academicyear.html",{'academicyeardata':academicyeardata})

def delacademicyear(request,did):
    tbl_academicyear.objects.get(id=did).delete()
    return render(request,"Admin/Academicyear.html",{'msg':"Data Deleted..."})

def Course(request):
    coursedata=tbl_course.objects.all()
    departmentdata=tbl_department.objects.all()
    if request.method=="POST":
        course=request.POST.get("txt_course")
        department=tbl_department.objects.get(id=request.POST.get("sel_department"))
        tbl_course.objects.create(course_name=course,department=department)
        return render(request,"Admin/Course.html",{'msg':"Data Inserted..."})
    else:
        return render(request,"Admin/Course.html",{'departmentdata':departmentdata,'coursedata':coursedata})

def delcourse(request,did):
    tbl_course.objects.get(id=did).delete()
    return render(request,"Admin/Course.html",{'msg':"Data Deleted..."})

def Subject(request):
    subjectdata=tbl_subject.objects.all()
    departmentdata=tbl_department.objects.all()
    semesterdata=tbl_semester.objects.all()
    if request.method=="POST":
        subject=request.POST.get("txt_subject")
        course=tbl_course.objects.get(id=request.POST.get("sel_course"))
        semester=tbl_semester.objects.get(id=request.POST.get("sel_semester"))
        tbl_subject.objects.create(subject_name=subject,course=course,semester=semester)
        return render(request,"Admin/Subject.html",{'msg':"Data Inserted..."})
    else:
        return render(request,"Admin/Subject.html",{'departmentdata':departmentdata,'semesterdata':semesterdata,'subjectdata':subjectdata})

def delsubject(request,did):
    tbl_subject.objects.get(id=did).delete()
    return render(request,"Admin/Subject.html",{'msg':"Data Deleted..."})

def Class(request):
    departmentdata=tbl_department.objects.all()
    classdata=tbl_class.objects.all()
    if request.method=="POST":
        name=request.POST.get("txt_class")
        course=tbl_course.objects.get(id=request.POST.get("sel_course"))
        tbl_class.objects.create(class_name=name,course=course)
        return render(request,"Admin/Class.html",{'msg':"Data Inserted..."})
    else:
        return render(request,"Admin/Class.html",{'departmentdata':departmentdata,'classdata':classdata})

def delclass(request,did):
    tbl_class.objects.get(id=did).delete()
    return render(request,"Admin/Class.html",{'msg':"Data Deleted..."})


def Addteacher(request):
    departmentdata=tbl_department.objects.all()
    teacherdata=tbl_teacher.objects.all()
    if request.method=="POST":
        name=request.POST.get("txt_name")
        email=request.POST.get("txt_email")
        contact=request.POST.get("txt_contact")
        role=request.POST.get("txt_role")
        gender=request.POST.get("txt_gender")
        photo= request.FILES.get("file_photo")
        password=request.POST.get("txt_password")
        department=tbl_department.objects.get(id=request.POST.get("sel_department"))
        tbl_teacher.objects.create(teacher_name=name,teacher_email=email,teacher_contact=contact,teacher_role=role,
        teacher_gender=gender,teacher_photo=photo,teacher_password=password,department=department)
        return render(request,"Admin/Addteacher.html",{'msg':"Data Inserted..."})
    else:
        return render(request,"Admin/Addteacher.html",{'departmentdata': departmentdata,'teacherdata':teacherdata})

def Assignclass(request,id):
    departmentdata=tbl_department.objects.all()
    academicyeardata=tbl_academicyear.objects.all()
    teacherid=tbl_teacher.objects.get(id=id)
    assignclassdata=tbl_assignclass.objects.filter(teacher=teacherid)
    if request.method=="POST":
        Class=tbl_class.objects.get(id=request.POST.get("sel_class"))
        year=tbl_academicyear.objects.get(id=request.POST.get("sel_academicyear"))
        tbl_assignclass.objects.create(Class=Class,academicyear=year,teacher=teacherid)
        return render(request,"Admin/Addteacher.html",{'msg':"Data Inserted..."})
    else:
        return render(request,"Admin/Assignclass.html",{'departmentdata':departmentdata,'academicyeardata':academicyeardata,
        'assignclassdata':assignclassdata})

def Assignsubject(request,id):
    departmentdata=tbl_department.objects.all()
    academicyeardata=tbl_academicyear.objects.all()
    semesterdata=tbl_semester.objects.all()
    teacherid=tbl_teacher.objects.get(id=id)
    assignsubjectdata=tbl_assignsubject.objects.filter(teacher=teacherid)
    if request.method=="POST":
        year=tbl_academicyear.objects.get(id=request.POST.get("sel_academicyear"))
        subjectid=tbl_subject.objects.get(id=request.POST.get("sel_subject"))
        tbl_assignsubject.objects.create(academicyear=year,teacher=teacherid,subject=subjectid)
        return render(request,"Admin/Addteacher.html",{'msg':"Data Inserted..."})
    else:
        return render(request,"Admin/Assignsubject.html",{'departmentdata':departmentdata,'academicyeardata':academicyeardata,
        'semesterdata':semesterdata,'assignsubjectdata':assignsubjectdata})




def Homepage(request):
    return render(request,"Admin/Homepage.html")

def Ajaxcourse(request):
    dep=tbl_department.objects.get(id=request.GET.get('disid'))
    course=tbl_course.objects.filter(department=dep)
    return render(request,'Admin/AjaxCourse.html',{'cs':course})

def Ajaxclass(request):
    course=tbl_course.objects.get(id=request.GET.get('clsid'))
    Class=tbl_class.objects.filter(course=course)
    return render(request,'Admin/AjaxClass.html',{'cls':Class})

def Ajaxsubject(request):
    sem=tbl_semester.objects.get(id=request.GET.get('subid'))
    course=tbl_course.objects.get(id=request.GET.get('coid'))
    sub=tbl_subject.objects.filter(semester=sem,course=course)
    print(sub)
    return render(request,'Admin/AjaxSubject.html',{'sub':sub})
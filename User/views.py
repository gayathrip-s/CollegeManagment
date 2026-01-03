from django.shortcuts import render
from Guest.models import *
from User.models import *
# Create your views here.
def Homepage(request):
 
  return render(request,"User/Homepage.html")

def Myprofile(request):
  userdata = tbl_user.objects.get(id=request.session['uid'])
  return render(request,"User/Myprofile.html",{'user':userdata})

def Editprofile(request):
  userdata = tbl_user.objects.get(id=request.session['uid'])
  if request.method == "POST":
    name=request.POST.get("txt_name")
    email=request.POST.get("txt_email")
    contact=request.POST.get("txt_contact")
    address=request.POST.get("txt_address")
        
    userdata.user_name = name
    userdata.user_email= email
    userdata.user_contact= contact
    userdata.user_address= address
    userdata.save()
    
    return render(request,"User/EditProfile.html",{'msg':"Data Updated..."})
  else:
    return render(request,"User/EditProfile.html",{'user':userdata})
 

def Changepass(request):
  userdata = tbl_user.objects.get(id=request.session['uid'])
  dbpass=userdata.user_password
  if request.method == "POST":
    password=request.POST.get("txt_password")
    newpassword=request.POST.get("txt_newpassword")
    repassword=request.POST.get("txt_repassword")  
    if dbpass==password:
      if newpassword==repassword:
        userdata.user_password = newpassword
        userdata.save()
        return render(request,"User/Changepass.html",{'msg':"Password changed..."})
      else:
        return render(request,"User/Changepass.html",{'msg':"Password does not match..."})
    else:
      return render(request,"User/Changepass.html",{'msg':"Invalid Old password..."})
  else:
    return render(request,"User/Changepass.html")
 
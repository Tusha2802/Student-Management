from django.shortcuts import render,redirect,HttpResponse
from student.models import Student,Course
from student.forms import StuForm,LoginForm,CourseForm
# Create your views here.

def profile(request):
     x=False;
     msg=''
     obj=Student()
     obj1=Course.objects.all()
     if request.method=="POST":
          form=StuForm(request.POST)
          if form.is_valid():
               cd=form.cleaned_data;
               obj.Name=cd['Name'];
               obj.Email=cd['Email'];
               obj.Password=cd['Password'];
               obj.Contact=cd['Contact'];
               obj.Qualification=cd['Qualification'];
               obj.save();
               #request.session['uname']=cd['Name']
               msg="You have Registered Successfully";
               x=True
               return redirect("/student/login/profile/abc")
               
     form=StuForm();
     return render(request,"student/profile.html",{'form':form,'x':x,'msg':msg,'id':id}) 
               
def login(request):
    #x=False
     msg=''
     if request.method=="POST":
          form=LoginForm(request.POST)
          if form.is_valid():
               cd=form.cleaned_data;
               btn=request.POST.get("btn")
               if(btn=="Admin"):
                    if(cd['UserName']=="Tushar@gmail.com" and cd['Password']=="Tushar"):
                         #b=Student.objects.all()
                         return render(request,"student/admin_index.html");
                    else:
                         msg="Error: Wrong UserName or Password";
               else:
                    w=Student.objects.get(Email=cd['UserName'],Password=cd['Password']);
                    if w:
                         request.session['uid']=w.id;
                         request.session['uname']=w.Name;
                         return redirect("/student/login/profile/abc")
                         #return render(request,"student/user_index.html",{'name':w.Name})
                    else:
                         msg="Error: Wrong UserName or Password";
               #x=True
     form=LoginForm();
     return render(request,"student/login.html",{'form':form,'msg':msg})


def admin_index(request):
     #b=Student.objects.all()
     return render(request,"student/admin_index.html")

def user_index(request):
     return render(request,"student/user_index.html")

def pcm(request):
     return render(request,"student/pcm.html")

def pcb(request):
     return render(request,"student/pcb.html")

def commerce(request):
     return render(request,"student/commerce.html")

def humanities(request):
     return render(request,"student/humanities.html")

def remove(request,stdid):
     r=Student.objects.get(id=stdid)
     r.delete()
     return redirect("/student/login/allUsers/")
def update(request,stdid):
     r=Student.objects.get(id=stdid)
     data={'Name':r.Name,'Email':r.Email,'Password':r.Password,'Contact':r.Contact,'Qualification':r.Qualification}
     form=StuForm(initial=data)
     if request.method=="POST":
          w=StuForm(request.POST)
          if w.is_valid():
               cd=w.cleaned_data;
               r.Name=cd['Name']
               r.Email=cd['Email']
               r.Password=cd['Password']
               r.Contact=cd['Contact']
               r.Qualification=cd['Qualification']
               r.save()
               return redirect("/student/login/allUsers/")

     return render(request,"student/profile.html",{'form':form})

def allUsers(request):
     b=Student.objects.all()
     return render(request,"student/allUsers.html",{'l':b})

def remove_all(request):
     r=Student.objects.all()
     r.delete()
     return render(request,"student/admin_index.html")


def course_start(request):
     x=False
     obj=Course()
     if request.method=="POST":
          form=CourseForm(request.POST)
          if form.is_valid():
               cd=form.cleaned_data;
               obj.c1=cd['c1']
               obj.c2=cd['c2']
               obj.c3=cd['c3']
               obj.c4=cd['c4']
               obj.save()
               x=True
     form=CourseForm()
     return render(request,"student/course_start.html",{'form':form,'x':x})

def abc(request):
     #msg=HttpResponse()
     x=False
     w=""
     obj=Course.objects.all()
     if request.method=="POST":
          for i in obj:
               w=request.POST.get(str(i.id))
          x=True
          return render(request,"student/user_index.html",{'id':w,'name':request.session['uname']})
     #msg.write("ok done !")
     form=CourseForm()
     return render(request,"student/abc.html",{'form':form,'id':w,'x':x,'l':obj})

def homepage(request):
     return render(request,"student/homepage.html")

def homepagemenu(request):
     return render(request,"student/homepagemenu.html")

def about_us(request):
     return render(request,"student/about_us.html")

def contact_us(request):
     return render(request,"student/contact_us.html")












               
          

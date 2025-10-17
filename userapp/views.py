from django.shortcuts import render
from .models import *
from django.http import HttpResponse
import datetime
from django.db import connection
from django.db.models import Q


# Create your views here.
def home(request):
    s = False
    if request.method == "POST":
        a = request.POST.get('name')
        b = request.POST.get('mob')
        c = request.POST.get('email')
        if (c.endswith('@email.com')):
           instantequiry(Name=a, Mobile=b, Email=c).save()
           s = True
        else:
            return HttpResponse("<script>alert('Email must be end with @email.com');window.location.href='user/index';</script>")
    return render(request, 'user/index.html', context={"email": s})
######################################################################################################
def login(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        currentuser=myregister.objects.filter(uname=email,passwd=password)
        print(currentuser)
        if currentuser:
            request.session['user']=email
            request.session['pic']=str(currentuser[0].pic)
            request.session['name']=str(currentuser[0].name)
            return HttpResponse("<script>alert('Login Successfully');window.location.href='/user/mail';</script>")
        else:
            return HttpResponse("<script>alert('Userid and password mismatch');window.location.href='/user/login';</script>")

    return render(request,'user/login.html')
#######################################################################################################
def signup(request):
    s=False
    if request.method=="POST":
        Name=request.POST.get('name')
        Email=request.POST.get('email')
        Password=request.POST.get('passwd')
        Address=request.POST.get('address')
        Picture=request.FILES.get('ppic')
        if(Email.endswith('@email.com')):
            myregister(name=Name,uname=Email,passwd=Password,address=Address,pic=Picture).save()
            s=True
        else:
            return HttpResponse("<script>alert('Email must should end with @email.com');window.location.href='user/signup';</script>")

    mydict={"status":s}

    return render(request,'user/signup.html',context=mydict)
##############################################################################################################

def contact(request):
    s=False
    if request.method=="POST":
        a=request.POST.get('name')
        b=request.POST.get('mob')
        c=request.POST.get('email')
        d=request.POST.get('msg')
        contactInfo(Name=a,Mobile=b,Email=c,Msg=d).save()
        s=True
    return render(request,'user/contact.html',context={"msg":s})
#########################################################################################################
def policy(request):
    return render(request,'user/policy.html')
################################################################################################
def sent(request):
    if request.session.get('user'):
        senderid = request.session.get('user')
        if request.GET.get('mid'):
            mid = request.GET.get('mid')
            cursor = connection.cursor()
            mail = message.objects.filter(id=mid)
            if mail[0].isstar == 'False':
                cursor.execute("update userapp_message set isstar='True' where id=" + mid + "")
            else:
                cursor.execute("update userapp_message set isstar='False' where id=" + mid + "")
        inbox = message.objects.filter(msgfrom=senderid, isdeleted='False', deletebysender=False).order_by('-id')
        if request.method == 'GET':
            searchkey = request.GET.get('searchkey')
            if searchkey is not None:
                inbox = message.objects.filter(Q(msgto=senderid) & (Q(msgtitle__icontains=searchkey) | Q(msgfrom__icontains=searchkey) | Q(msgdesc__icontains=searchkey) | Q(msgtime__icontains=searchkey)))
        i = 0
        for row in inbox:
            if len(row.msgdesc) > 80:
                inbox[i].msgdesc = inbox[i].msgdesc[0:80] + '......'
            i = i + 1

        if request.method == 'POST':
            receiverid = request.POST.get('recmail')
            mailtitle = request.POST.get('title')
            mailmsg = request.POST.get('message')
            mailattach = request.FILES.get('mailfile')
            message(msgfrom=senderid, msgto=receiverid, msgtitle=mailtitle, msgdesc=mailmsg,
                    msgtime=datetime.datetime.now(), status='True', isstar='False', isdeleted='False',
                    msgfile=mailattach).save()
            return HttpResponse("<script>alert('Mail Sent Successfully');window.location.href='/user/sent';</script>")
        return render(request, 'user/sent.html', {'inbox': inbox})
    else:
        return HttpResponse("<script>alert('Login First to access mail');window.location.href='user/login';</script>")
##############################################################################################################
def mail(request):
    if request.session.get('user'):
      senderid=request.session.get('user')
      if request.GET.get('mid'):
          mid=request.GET.get('mid')
          cursor=connection.cursor()
          mail=message.objects.filter(id=mid)
          if mail[0].isstar == 'False':
             cursor.execute("update userapp_message set isstar='True' where id="+mid+"")
          else:
              cursor.execute("update userapp_message set isstar='False' where id=" + mid + "")

      inbox=message.objects.filter(msgto=senderid,isdeleted='False',deletebyrec=False).order_by('-id')
      if request.method == 'GET':
          searchkey=request.GET.get('searchkey')
          if searchkey is not None :
              inbox=message.objects.filter(Q(msgto=senderid) &  (Q(msgtitle__icontains=searchkey) | Q(msgfrom__icontains=searchkey) | Q(msgdesc__icontains=searchkey) | Q(msgfrom__icontains=searchkey)))
      i=0
      for row in inbox:
          if len(row.msgdesc)>80:
              inbox[i].msgdesc=inbox[i].msgdesc[0:80]+'......'
          i=i+1


      if request.method=='POST':
         receiverid=request.POST.get('recmail')
         mailtitle=request.POST.get('title')
         mailmsg=request.POST.get('message')
         mailattach=request.FILES.get('mailfile')
         message( msgfrom=senderid, msgto=receiverid, msgtitle=mailtitle, msgdesc=mailmsg, msgtime=datetime.datetime.now(), status='True', isstar='False', isdeleted='False', msgfile=mailattach).save()
         return HttpResponse("<script>alert('Mail Sent Successfully');window.location.href='/user/mail';</script>")
      return render(request,'user/mail.html',{'inbox':inbox})
    else:
         return HttpResponse("<script>alert('Login First to access mail');window.location.href='user/login';</script>")
################################################################################################
def favourite(request):
    if request.session.get('user'):
        senderid = request.session.get('user')
        if request.GET.get('mid'):
            mid = request.GET.get('mid')
            cursor = connection.cursor()
            mail = message.objects.filter(id=mid)
            if mail[0].isstar == 'False':
                cursor.execute("update userapp_message set isstar='True' where id=" + mid + "")
            else:
                cursor.execute("update userapp_message set isstar='False' where id=" + mid + "")

        inbox = message.objects.filter(msgto=senderid, isdeleted='False',isstar='True').order_by('-id')
        if request.method == 'GET':
            searchkey = request.GET.get('searchkey')
            if searchkey is not None:
                inbox = message.objects.filter(Q(msgto=senderid) & (Q(msgtitle__icontains=searchkey) | Q(msgfrom__icontains=searchkey) | Q(msgdesc__icontains=searchkey) | Q(msgfrom__icontains=searchkey)))
        i = 0
        for row in inbox:
            if len(row.msgdesc) > 80:
                inbox[i].msgdesc = inbox[i].msgdesc[0:80] + '......'
            i = i + 1

        if request.method == 'POST':
            receiverid = request.POST.get('recmail')
            mailtitle = request.POST.get('title')
            mailmsg = request.POST.get('message')
            mailattach = request.FILES.get('mailfile')
            message(msgfrom=senderid, msgto=receiverid, msgtitle=mailtitle, msgdesc=mailmsg,
                    msgtime=datetime.datetime.now(), status='True', isstar='False', isdeleted='False',
                    msgfile=mailattach).save()
            return HttpResponse("<script>alert('Mail Sent Successfully');window.location.href='/user/favourite';</script>")
        return render(request, 'user/favourite.html', {'inbox': inbox})
    else:
        return HttpResponse("<script>alert('Login First to access mail');window.location.href='user/login';</script>")

######################################################################
def msgdetail(request):
    if request.GET.get('mid'):
        if request.GET.get('type'):
            mid=request.GET.get('mid')
            type=request.GET.get('type')
            cursor=connection.cursor()
            if type == 'sender':
                cursor.execute("select u.name,u.uname,u.pic,m.msgtitle,m.msgdesc,m.msgtime from userapp_myregister u,userapp_message m where m.id="+mid+" and m.msgfrom=u.uname")
            elif type == 'rec':
                cursor.execute("select u.name,u.uname,u.pic,m.msgtitle,m.msgdesc,m.msgtime from userapp_myregister u,userapp_message m where m.id="+mid+" and m.msgto=u.uname")
            msgdetail=cursor.fetchall()
            return render(request, 'user/msgdetail.html',{'msgdetail':msgdetail})
    else:
        return HttpResponse("<script>alert('Some parameter are missing.Please try again.');window.location.href='user/mail';</script>")

########################################################################################################
def gallery(request):
    x=ugallery.objects.all().order_by('-id')
    mydict={"data":x}
    return render(request,'user/gallery.html',mydict)
######################################################################################################
def logout(request):
      del request.session['user']
      del request.session['name']
      del request.session['pic']
      return HttpResponse("<script>window.location.href='/user/login'</script>")
####################################################################################################
def ranjan(request):
    return render(request,'user/ranjan.html')
######################################################################################################

def deletemail(request):
    if request.GET.get('mid'):
        if request.GET.get('type'):
            mid=request.GET.get('mid')
            type=request.GET.get('type')
            cursor=connection.cursor()
            if type == 'sender':
                cursor.execute("update userapp_message set deletebyrec=True where id="+mid+"")
            elif type == 'rec':
                cursor.execute("update userapp_message set deletebysender=True where id="+mid+"")
            return HttpResponse("<script>alert('Mail deleted');window.location.href='/user/mail';</script>")
    else:
        return HttpResponse("<script>alert('Some parameter are missing.Please try again.');window.location.href='/user/mail';</script>")

############################################################################################################
def bin(request):
    if request.session.get('user'):
        senderid = request.session.get('user')

        inbox = message.objects.filter(msgto=senderid, isdeleted='False', deletebyrec=True, deletebysender=True).order_by('-id')
        i = 0
        for row in inbox:
            if len(row.msgdesc) > 80:
                inbox[i].msgdesc = inbox[i].msgdesc[0:80] + '......'
            i = i + 1

        if request.method == 'POST':
            receiverid = request.POST.get('recmail')
            mailtitle = request.POST.get('title')
            mailmsg = request.POST.get('message')
            mailattach = request.FILES.get('mailfile')
            message(msgfrom=senderid, msgto=receiverid, msgtitle=mailtitle, msgdesc=mailmsg,
                    msgtime=datetime.datetime.now(), status='True', isstar='False', isdeleted='False',
                    msgfile=mailattach).save()
            return HttpResponse("<script>alert('Mail Sent Successfully');window.location.href='/user/bin';</script>")
        return render(request, 'user/bin.html', {'inbox': inbox})
    else:
        return HttpResponse("<script>alert('Login First to access mail');window.location.href='user/bin';</script>")
######################################################################################################################
def changepasswd(request):
    s = False
    if request.method == "POST":
        a = request.POST.get('opasswd')
        b = request.POST.get('npasswd')
        c = request.POST.get('npasswd')
        changepassword(Opassword=a, Npassword=b, Cpassword=c ).save()
        s = True

    return render(request, 'user/changepasswd.html', context={"opassword": s})


######################################################################################################################
def forgetpasswd(request):
    s = False
    if request.method == "POST":
        a = request.POST.get('email')
        b = request.POST.get('passwd')
        if (a.endswith('@email.com')):
           resetpasswd(Email=a, Password=b,).save()
           s = True
        else:
            return HttpResponse("<script>alert('Email must be end with @email.com');window.location.href='user/forgetpasswd';</script>")
    return render(request,'user/forgetpasswd.html',context={"email": s})
##########################################################################################################################
def feedback(request):
    s = False
    if request.method == "POST":
        a = request.POST.get('name')
        b = request.POST.get('location')
        c = request.POST.get('email')
        d = request.POST.get('feedback')
        feedbackopt(Name=a, Location=b, Email=c, Feedback=d).save()
        s = True
    return render(request, 'user/feedback.html', context={"feedback": s})


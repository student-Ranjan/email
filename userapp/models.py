from django.db import models

# Create your models here.
class contactInfo(models.Model):
    Name=models.CharField(max_length=80)
    Email=models.CharField(max_length=30)
    Mobile=models.CharField(max_length=40)
    Msg=models.TextField()
    def __str__(self):
        return self.Name
###################################################################################################################
class ugallery(models.Model):
    gdes=models.CharField(max_length=200)
    picture=models.ImageField(upload_to='static/gallery/',default="null")

####################################################################################################################
class myregister(models.Model):
    name=models.CharField(max_length=100)
    uname=models.CharField(max_length=120,primary_key=True)
    passwd=models.CharField(max_length=200)
    address=models.TextField()
    pic=models.ImageField(upload_to='static/profile/')
######################################################################################################

class message(models.Model):
    msgfrom=models.CharField(max_length=100)
    msgto=models.CharField(max_length=100)
    msgtitle=models.CharField(max_length=300)
    msgdesc=models.TextField()
    msgtime=models.DateField()
    status=models.CharField(max_length=20)
    isstar=models.CharField(max_length=20)
    isdeleted=models.CharField(max_length=20)
    msgfile=models.ImageField(upload_to='static/msgfile/',null=True)
    deletebysender=models.BooleanField(default=False)
    deletebyrec=models.BooleanField(default=False)
#####################################################################################################
class instantequiry(models.Model):
    Name=models.CharField(max_length=80)
    Email=models.CharField(max_length=30)
    Mobile=models.CharField(max_length=40)
#############################################################################################################
class resetpasswd(models.Model):
    Email=models.CharField(max_length=30)
    Password=models.CharField(max_length=150)
##############################################################################################################
class changepassword(models.Model):
    Opassword=models.CharField(max_length=150)
    Npassword=models.CharField(max_length=150)
    Cpassword=models.CharField(max_length=150)
####################################################################################################################

class feedbackopt(models.Model):
    Name=models.CharField(max_length=80)
    Email=models.CharField(max_length=30)
    Location=models.CharField(max_length=500)
    Feedback=models.TextField()

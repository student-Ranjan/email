from django.contrib import admin
from .models import *

class contactInfoAdmin(admin.ModelAdmin):
    list_display = ('Name','Mobile','Email','Msg')

admin.site.register(contactInfo,contactInfoAdmin)
##########################################################################################

class ugalleryAdmin(admin.ModelAdmin):
    list_display = ('id','gdes','picture')

admin.site.register(ugallery,ugalleryAdmin)


#########################################################################################

class myregisterAdmin(admin.ModelAdmin):
    list_display = ('name','uname','passwd','address','pic')

admin.site.register(myregister,myregisterAdmin)
# Register your models here.

##############################################################################################

class registermsgAdmin(admin.ModelAdmin):
    list_display = ('id','msgfrom','msgto','msgtitle','msgdesc','msgtime','status','isstar','isdeleted','msgfile','deletebysender','deletebyrec')

admin.site.register(message,registermsgAdmin)
##########################################################################################################

class instantequiryAdmin(admin.ModelAdmin):
    list_display = ('Name','Mobile','Email')

admin.site.register(instantequiry,instantequiryAdmin)
#############################################################################################################
class resetpasswdAdmin(admin.ModelAdmin):
    list_display = ('Email','Password')

admin.site.register(resetpasswd,resetpasswdAdmin)
###############################################################################################################
class changepasswordAdmin(admin.ModelAdmin):
    list_display = ('Opassword','Npassword','Cpassword')

admin.site.register(changepassword,changepasswordAdmin)
###############################################################################################################
class feedbackoptAdmin(admin.ModelAdmin):
    list_display = ('Name','Location','Email','Feedback')

admin.site.register(feedbackopt,feedbackoptAdmin)
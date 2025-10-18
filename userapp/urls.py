from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('home/',views.home),
    path('',views.home),
    path('login/',views.login),
    path('signup/',views.signup),
    path('contact/',views.contact),
    path('policy/',views.policy),
    path('gallery/',views.gallery),
    path('feedback/',views.feedback),
    path('mail/',views.mail),
    path('logout/',views.logout),
    path('msgdetail/',views.msgdetail),
    path('favourite/',views.favourite),
    path('sent/',views.sent),
    path('ranjan/',views.ranjan),
    path('deletemail/',views.deletemail),
    path('bin/',views.bin),
    path('changepasswd/',views.changepasswd),
    path('forgetpasswd/',views.forgetpasswd),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
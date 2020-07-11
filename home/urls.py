from django.urls import path

from home import views

urlpatterns = [
   path('',views.index,name='mysite'),
   path('showproject/<str:pk>',views.showProject,name='viewProject'),
   path('contact',views.contactme,name='contact'),
   path('thankyou',views.thankyou,name='thankyou')

]


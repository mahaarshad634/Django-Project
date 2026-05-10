from django.contrib import admin
from django.urls import path
from myapp import views
urlpatterns = [
    path('', views.home , name="home"),
    path('pro/',views.product,name="product"),
    path('about/',views.aboutus, name='aboutus'),
    path('con/',views.contact_view,name='contact'),
    path('delete/<int:id>/', views.delete, name='delete'),
     path('addpost/', views.addpost, name= 'addpost'),
 path('updatepost/', views.updatepost, name='updatepost'),

]

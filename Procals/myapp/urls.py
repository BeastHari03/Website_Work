from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.index, name="index"),
    path('register/',views.register, name="register"),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),


]
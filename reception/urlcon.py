from django.urls import path
from . import views
urlpatterns=[path('home/',views.say_hi,name='home'),
            path('home/add',views.add,name='add')]

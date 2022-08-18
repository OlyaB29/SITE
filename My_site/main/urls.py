from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('contacts/',views.contacts,name='contacts'),
    path('about-us',views.about,name='about'),
    path('YDC',views.YDC,name='YDC'),
    path('create',views.create,name='create')
]
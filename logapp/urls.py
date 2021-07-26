from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('signup/',views.signup,name='signup'),
    path('signup_save/',views.signup_save,name='signup_save'),
    path('login/',views.login,name='login'),
    path('login_save/',views.login_save,name='login_save'),
]
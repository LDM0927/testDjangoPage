from django.urls import path
from .views import signupfunc
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', signupfunc, name='signup'),
]

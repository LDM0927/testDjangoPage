from django.urls import path
from .views import signupfunc, loginfunc, userpagefunc
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('userpage/', userpagefunc, name='userpage'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.indexfunc, name='index'),
    path('signup/', views.signupfunc, name='signup'),
    path('login/', views.loginfunc, name='login'),
    path('userpage/', views.userpagefunc, name='userpage'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

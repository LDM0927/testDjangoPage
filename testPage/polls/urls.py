from django.urls import path
from .views import signupfunc
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', signupfunc, name='signup'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

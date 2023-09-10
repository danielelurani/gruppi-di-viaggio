from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('organizzatoreViaggi/signup', views.signup_view, name='signup'),
]
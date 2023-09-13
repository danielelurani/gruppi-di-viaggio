from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path("logout/", views.logout_user, name='logout'),
    path('organizzatoreViaggi/signup', views.signup_view, name='signup'),
    path('organizzatoreViaggi/detailsTravel', views.detailsTravel_view, name='detailsTravel'),
    path('organizzatoreViaggi/myTravels', views.myTravels_view, name='myTravels'),
    path('organizzatoreViaggi/changeItinerary', views.changeItinerary_view, name='changeItinerary'),
    path('organizzatoreViaggi/userHomePage', views.userHomePage_view, name='userHomePage')

]
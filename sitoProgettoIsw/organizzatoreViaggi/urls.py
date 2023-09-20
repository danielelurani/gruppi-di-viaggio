from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path("logout/", views.logout_user, name='logout'),
    path('organizzatoreViaggi/signup', views.signup_view, name='signup'),
    path('organizzatoreViaggi/detailsTravel/<int:travel_id>/', views.detailsTravel_view, name='detailsTravel'),
    path('organizzatoreViaggi/myTravels', views.myTravels_view, name='myTravels'),
    path('organizzatoreViaggi/changeItinerary/<int:travel_id>/', views.changeItinerary_view, name='changeItinerary'),
    path('organizzatoreViaggi/userHomePage', views.userHomePage_view, name='userHomePage'),
    path('organizzatoreViaggi/invite', views.invite_view, name='invite'),
    path('organizzatoreViaggi/expenses/<int:travel_id>/', views.expenses_view, name='expenses'),
    path('organizzatoreViaggi/processInvitation_view/<int:inv_id>/', views.processInvitation_view, name='processInvitation'),
    path('organizzatoreViaggi/addComment_view/<int:travel_id>/', views.addComment_view, name='addComment'),
    path('organizzatoreViaggi/addExpense_view/<int:travel_id>/', views.addExpense_view, name='addExpense')
]
from django.urls import path
from . import views

app_name = 'loan'
urlpatterns = [
    path('sign up', views.create_user, name='create_user'),
    path('login', views.login_page, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('', views.index, name='home'),
    path('prediction/', views.prediction, name='prediction'),
    path('successful predictions/', views.successful_predictions, name='prediction_detail'),
    path('about/', views.about, name='about_us'),
    path('help/', views.help, name='help'),
    path('<int:pk>/help_detail/', views.help_detail, name='help_detail'),
    path('T&C/', views.terms_policy, name='terms_policy'),
]
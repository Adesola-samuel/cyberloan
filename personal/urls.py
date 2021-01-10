from django.urls import path
from . import views

app_name = 'profile'
urlpatterns = [
    path('update', views.update, name='update'),
    path('profile/<int:id>/', views.profile, name='user-profile'),
    path('portfolio-detail/<int:id>/', views.portfolio_detail, name='portfolio-detail'),
    path('ID-Card', views.card, name='card'),
]
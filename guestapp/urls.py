from django.urls import path
from . import views
app_name = 'guestapp'
urlpatterns = [
    path('', views.home_page, name='home-page'),
    
]

from django.urls import path
from .import views
urlpatterns = [
    path('', views.home,name='portfolio-home'),
    path('main/', views.main,name='portfolio-main'),
    path('about/', views.about,name='portfolio-about'),
    path('contact/', views.contact,name='portfolio-contact'),

]
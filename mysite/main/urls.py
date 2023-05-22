from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('booking/', views.booking, name='booking'),
        path('contact/', views.contact, name='contact'),
        path('menu/', views.menu, name='menu'),
        path('service/', views.service, name='service'),
        path('team/', views.team, name='team'),
        path('about/', views.about, name='about'),
        path('testimonial/', views.testimonial, name='testimonial'),
        path('answer/', views.answer, name='answer'),
        path('register/', views.register_request, name='register'),
        path('login/', views.login_request, name='login'),
        path('logout/', views.logout_request, name='logout'),
        path(r'activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',  views.activate, name='activate'),

]

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from user.models import MpesaPayment,User
from . import views
from rest_framework.routers import DefaultRouter
from .views import  MpesaPaymentViewSet, activate, SignUpViewSet, UpdateUserProfileViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Job', views.JobViewSet)
router.register('MpesaPayment', views.MpesaPaymentViewSet)
router.register('User', views.SignUpViewSet)
router.register('UpdateUserProfile', views. UpdateUserProfileViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('MpesaPayment/', views.MpesaPayment, name='MpesaPayment'),
    path('job/', views.Job, name='Job'),
    path('user/', views.User, name='User'),
    path('profile/', views.Profile, name='UpdateUserProfile'),
    path('activate/(<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',  
        activate, name='activate'),  
    path('profile/', views.Profile, name='UpdateUserProfile'),
    path('employer-list/', views.employerList, name='employer-list'),
    path('employer-detail/<str:pk>/', views.employerDetail, name='employer-detail'),
    path('employer-profile-create/', views.employerProfileCreate, name='employer-profile-create'),
    
   
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
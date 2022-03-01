from django.urls import path
from .views import HomePageView, AboutPageView,SupportPageView,PrivacyPolicuPageView

urlpatterns = [
    path("support/", PrivacyPolicuPageView.as_view(), name='privacy'),
    path("privacy/", SupportPageView.as_view(), name='support'),
    path("about/",AboutPageView.as_view(), name='about'),
    path('',HomePageView.as_view(), name='home'),
]

from django.views.generic import  TemplateView

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class SupportPageView(TemplateView):
    template_name = 'support.html'

class PrivacyPolicuPageView(TemplateView):
    template_name = 'privacyPolicy.html'


from django.views.generic.base import RedirectView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeRedirectView(RedirectView):
    permanent = True
    pattern_name = 'dashboard'


class DashboardView(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    template_name = "core/dashboard.html"
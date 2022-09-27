from django.views.generic.base import RedirectView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from allauth.account.views import LoginView, LogoutView, SignupView
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class AccountLoginView(LoginView):
    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        ret = super(LoginView, self).get_context_data(**kwargs)
        return ret


class AccountLogoutView(LogoutView):
    def get_context_data(self, **kwargs):
        ret = super(LogoutView, self).get_context_data(**kwargs)
        return ret


class AccountSignupView(SignupView):
    template_name = 'signup.html'

    def get_context_data(self, **kwargs):
        ret = super(SignupView, self).get_context_data(**kwargs)
        return ret


class HomeRedirectView(RedirectView):
    permanent = True
    pattern_name = 'dashboard'


class DashboardView(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    template_name = "dashboard.html"
from allauth.account.views import LoginView, LogoutView

class AccountLoginView(LoginView):
    template_name = 'accounts/login.html'

    def get_context_data(self, **kwargs):
            ret = super(LoginView, self).get_context_data(**kwargs)
            return ret

class AccountLogoutView(LogoutView):
    def get_context_data(self, **kwargs):
            ret = super(LogoutView, self).get_context_data(**kwargs)
            return ret
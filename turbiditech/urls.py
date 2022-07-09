from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from api.views import UserViewSet, GroupViewSet
from accounts.views import AccountLoginView, AccountLogoutView
from core.views import  HomeRedirectView, DashboardView

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('login/', AccountLoginView.as_view(), name='account_login'),
    path('logout/', AccountLogoutView.as_view()),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('', HomeRedirectView.as_view()),
]
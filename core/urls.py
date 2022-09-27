from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('login/', views.AccountLoginView.as_view(), name='account_login'),
    path('logout/', views.AccountLogoutView.as_view(), name='account_logout'),
    path('signup/', views.AccountSignupView.as_view(), name='account_signup'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('', views.HomeRedirectView.as_view()),
]

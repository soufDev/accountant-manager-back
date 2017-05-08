from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token

from djoser import views
from authentication.models import Account

urlpatterns = [
    url(r'^login/', obtain_jwt_token),
    url(r'^logout/', views.LogoutView.as_view(), name='logout'),
    url(r'^me/', views.UserView.as_view(), name='user'),
    url(r'^register/', views.RegistrationView.as_view(), name='register'),
    url(r'^activate/', views.ActivationView.as_view(), name='activate'),
    url(r'^{0}/'.format(Account.USERNAME_FIELD), views.SetUsernameView.as_view(), name='set_username'),
    url(r'^password/', views.SetPasswordView.as_view(), name='set_password'),
    url(r'^password/reset/', views.PasswordResetView.as_view(), name='password_reset'),
    url(r'^password/reset/confirm/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

]

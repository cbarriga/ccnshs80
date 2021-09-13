from django.contrib.auth import views as auth_views
from django.urls import path
from profiles.forms import LoginForm
from profiles.views import ChangePasswordView, CustomLoginView, ResetPasswordView

from .views import home_view, RegisterView, profile

urlpatterns = [
    path('', home_view, name='profiles-home'),
    path('register/', RegisterView.as_view(), name='profiles-register'),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='profiles/login.html',
                                           authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='profiles/logout.html'), name='logout'),
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='profiles/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='profiles/password_reset_complete.html'),
         name='password_reset_complete'),
    path('profile/', profile, name='profiles-profile'),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),
]
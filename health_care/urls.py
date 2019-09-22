"""health_care URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib import admin
from bloodcare.views import user_register, hospital_register, bank_register, home, dashboard, search_alert, use, donate
from django.urls import path, include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('user-register/', user_register, name='user_register'),
    path('hospital-register/', hospital_register, name='hospital_register'),
    path('bank-register/', bank_register, name='bank_register'),
    path('home/', home, name='home'),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True,
                                                template_name='bloodcare/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='bloodcare/logout.html'), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='bloodcare/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='bloodcare/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='bloodcare/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='bloodcare/password_reset_complete.html'), name='password_reset_complete'),

    path('dashboard/', dashboard, name='dashboard'),
    path('search-alert/', search_alert, name='search_alert'),
    path('use/', use, name='use'),
    path('donate/', donate, name='donate'),
]

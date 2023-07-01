"""global_search URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from global_search.core.views.auto_suggest import AutoSuggestAPI
from global_search.core.views.dashboard import dashboard_page
from global_search.core.views.detail import DetailAPI, detail_page
from global_search.core.views.login import LoginAPI, login_page
from global_search.core.views.login_otp_send import EmailLoginSendOTPAPI
from global_search.core.views.logout import LogoutAPI
from global_search.core.views.mobile_otp_send import MobileLoginSendOTPAPI
from global_search.core.views.result import result_page
from global_search.core.views.search import SearchAPI
from global_search.core.views.signup import SignupAPI, signup_page

urlpatterns = [
    path("admin/", admin.site.urls),
    path("signup/", signup_page, name="signup"),
    path("login/", login_page, name="login"),
    path("logout/", LogoutAPI.as_view(), name="logout"),
    path("dashboard/", dashboard_page, name="dashboard"),
    path("results/", result_page, name="results"),
    path("detail/", detail_page, name="detail"),
    path("api/v1/signup/", SignupAPI.as_view(), name="signup-api"),
    path(
        "api/v1/login/email/send/otp/",
        EmailLoginSendOTPAPI.as_view(),
        name="email-login-otp-send-api",
    ),
    path(
        "api/v1/login/mobile/send/otp/",
        MobileLoginSendOTPAPI.as_view(),
        name="mobile-login-otp-send-api",
    ),
    path("api/v1/login/", LoginAPI.as_view(), name="signup-api"),
    path("api/v1/autosuggest/", AutoSuggestAPI.as_view(), name="autosuggest-api"),
    path("api/v1/search/", SearchAPI.as_view(), name="search-api"),
    path("api/v1/details/", DetailAPI.as_view(), name="detail-api"),
]

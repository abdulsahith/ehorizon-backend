"""
URL configuration for ehorizon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.conf import settings
from app.views import (
    pitch_register,
    gameathon_register,
    buildscape_register,
    webify_register,
    electric_register,
    ipl_register,
    master_register,
    mech_register,
    thirai_register,
    talentia_register,
    admin_login,
    rising_register,
    startup_register,
    ipr_register,
    business_register,
    product_register,
    stocks_register,
    bplan_register,
    detx_register,
)

from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("pitch/register/", pitch_register),
    path("gameathon/register/", gameathon_register),
    path("buildscape/register/", buildscape_register),
    path("webify/register/", webify_register),
    path("electrical-odyssey/register/", electric_register),
    path("ipl-auction/register/", ipl_register),
    path("masterchef-mania/register/", master_register),
    path("mecharena/register/", mech_register),
    path("thirai-trivia/register/", thirai_register),
    path("adminlogin/",admin_login),
    path("talentia/register/", talentia_register),
    path("rising-capital-finance/register/",rising_register),
    path("startup-legal-ethical/register/",startup_register),
    path("ipr-ip-management/register/",ipr_register),
    path("business-market-fit/register/",business_register),
    path("product-market-fit/register/",product_register),
    path("stocks-shares/register/",stocks_register),
    path("b-plan/register/",bplan_register),
    path("detx-forum/register/",detx_register),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
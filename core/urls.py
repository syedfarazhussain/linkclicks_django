# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("apps.authentication.urls")), # Auth routes - login / register

    # ADD NEW Routes HERE
	path("google_ads/", include("apps.google_ads.urls")),
  	path("meta/", include("apps.meta.urls")),
	path("pinterest/", include("apps.pinterest.urls")),

    # Leave `Home.Urls` as last the last line
    path("", include("apps.home.urls"))
]

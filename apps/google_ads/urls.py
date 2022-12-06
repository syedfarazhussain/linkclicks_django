# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.google_ads import views

urlpatterns = [
	path('ad-campaign-create',views.ad_campaign_create,name='ad-campaign-create'),
	path('enable',views.enable,name='enable'),
	path('disable',views.disable,name='disable'),
	path('oauth',views.oauth,name='oauth'),
]

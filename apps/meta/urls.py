# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from apps.meta import views

urlpatterns = [

    path('enable',views.enable,name='enable'),
	path('disable',views.disable,name='disable'),
	path('oauth/',views.oauth,name='oauth'),
]

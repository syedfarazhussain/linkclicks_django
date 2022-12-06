# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from datetime import datetime
import random
import ast
import json
import os
import sys
import uuid

from .models import *

@login_required(login_url="/login/")
def ad_accounts(request):

	try:
		context = {}
		if request.method == "POST":
			account= request.POST["account"]
			account = ast.literal_eval(account)
			account = json.loads(json.dumps(account))
			print(account)
			
			ad_platform= request.POST["ad_platform"]
			
			authorization = Authorizations.objects.filter(user=request.user, account_id=None, ad_platform=ad_platform).update(account_id=account['account_id'], account_name=account['account_name'], date_time=datetime.utcnow(), )

		current_user = request.user
		
		authorized_platforms_list = list(Authorizations.objects.filter(user=current_user).exclude(account_id__isnull=True).all())
		print(authorized_platforms_list)
		
		authorized_platforms = {}
		print('FOR PLATFORM IN AUTH')
		for i in authorized_platforms_list:
			print("PLATFORM!!!")
			print(i.ad_platform)
			authorized_platforms[i.ad_platform] = i.account_name

		context['authorized_platforms'] = authorized_platforms
		print('authorized platforms')
		print(authorized_platforms)
		context['segment'] = 'ad-accounts'
		context['title'] = 'Connected ad accounts'

		
		html_template = loader.get_template('home/ad-accounts.html')
		return HttpResponse(html_template.render(context, request))
	
	except Exception as e:
		print(e)
		exc_type, exc_obj, exc_tb = sys.exc_info()
		fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
		fpath = os.path.split(exc_tb.tb_frame.f_code.co_filename)[0]
		print('ERROR', exc_type, fpath, fname, 'on line', exc_tb.tb_lineno)
		html_template = loader.get_template('home/page-500.html')
		return HttpResponse(html_template.render(request))
	


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

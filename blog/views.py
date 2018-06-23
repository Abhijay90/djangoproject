# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.views import APIView
# from rest_framework.response import Response
from django.http import JsonResponse

from .service import *


class initClass(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # queryset = User.objects.all().order_by('-date_joined')
    def get(self,request):
    	print "why"
    	return JsonResponse({'some': 'data'})

    def post(self,request):
    	print "why not"
    	return JsonResponse({'some': 'data'})
# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
#from django.shortcuts import render
from django.http import HttpResponse
#from django.http import *
from django.shortcuts import *
import os
from subprocess import *
from nh import *

# Create your views here.
def hello(request):
    return HttpResponse('Hello World ! ')

#http://192.168.136.247/host/search
def input_ip(request):
     if request.method == 'GET':
        a = request.GET['search']
        result = input1_ip(a)
        result2 = "nexthop {}".format(result)
        return HttpResponse(result2, content_type='text/plain')
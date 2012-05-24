#!/usr/bin/python
#coding:utf-8
from django.http import HttpResponse as response
from django.shortcuts import render_to_response as render
from django.template.context import RequestContext as rc
from django.shortcuts import get_object_or_404 as get_or_404
from julet.weddings import wedding_code
from julet.weddings.models import Wedding
# Create your views here.

def index(request):
    weddings = Wedding.objects.all()[:5]
    args = {'id':wedding_code(), 'weddings':weddings}
    return render('index.html', args, context_instance=rc(request))

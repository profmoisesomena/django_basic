# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Question


def index(request):
    latest_question_list = Question.objects.all()
    var_get_search = request.GET.get('search_box')
    if var_get_search is not None:
        latest_question_list = latest_question_list.filter(question_text__icontains =var_get_search)
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/busca.html', context)


def busca(request):
    quest =  Question.objects.all()
    var_get_search = request.GET.get('search_box')
    if var_get_search  is not None:
        quest = quest.filter(question_text__icontains =var_get_search)
    return render(request, 'polls/busca.html',{'quest':quest})
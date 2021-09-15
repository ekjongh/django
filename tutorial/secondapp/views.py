from django.http.response import JsonResponse
from django.shortcuts import render

from django.http import HttpResponse

def main(request): # request 파라미터 필수
    # do something....
    return HttpResponse('<u>Second Main</u>')

from .models import Course
def insert(request): # request 파라미터 필수
    # do something....
    # Create
    Course.objects.create(name='데이터 분석', cnt=30)
    # Save
    Course(name='웹 개발', cnt=25).save()
    Course(name='인공지능', cnt=20).save()

    return HttpResponse('<u>Second Insert</u>')

def show(request):
    course = Course.objects.all()
    print(course)
    context = {
        'data' : course
    }
    return render(request, 'secondapp/show.html', context)
    # result = ''
    # for c in course:
    #     # result += c.name + '/'<br>'
    #     result += f"{c.name} / {c.cnt} <br>"
    # return HttpResponse(result)

from .models import AmyShop
def showArmyShop(request):
    prd = request.GET.get('prd')
    course = AmyShop.objects.filter(name__contains=prd)
    print(course)
    context = {
        'data' : course
    }
    return render(request, 'secondapp/showArmyShop.html', context)

def showArmyShop2(request, year, month):
    course = AmyShop.objects.filter(year=year, month=month)
    print(course)
    context = {
        'data' : course
    }
    return render(request, 'secondapp/showArmyShop.html', context)

    
def req_ajax(request):
    return render(request, 'secondapp/ajax.html')

def req_ajax_get(request):
    print("req_ajax_get")
    a = request.GET.get('a')
    b = request.GET.get('b')
    c = request.GET.get('c')
    # c = request.GET['c'] # get() 에러 없음
    #                      # GET['c'] 에러가 날 수 있음
    result = '%s %s %s' % (a, b, c)
    return HttpResponse(result)

def req_ajax_post(request):
    print("req_ajax_get")
    a = request.GET.get('a')
    b = request.GET.get('b')
    c = request.GET.get('c')
    # c = request.GET['c'] # get() 에러 없음
    #                      # GET['c'] 에러가 날 수 있음
    result = '%s %s %s' % (a, b, c)
    return HttpResponse(result)

import json
from django.forms.models import model_to_dict
def req_ajax_json(request):
    obj = request.body.decode("utf-8")
    data = json.loads(obj)

    co = Course.objects.all()
    c_list = []
    for c in co:
            c = model_to_dict(c)
            c_list.append(c)
    
    return JsonResponse(c_list, safe=False)



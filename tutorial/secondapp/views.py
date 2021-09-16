from django.http.response import JsonResponse
from django.shortcuts import redirect, render

from django.http import HttpResponse

def main(request): # request 파라미터 필수
    # do something....
    return render(request, 'secondapp/main.html')
    # return HttpResponse('<u>Second Main</u>')

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
    # prd = request.GET.get('prd', '')
    prd = request.GET.get('prd') # None(X)
    if not prd:
        prd = ''
    shop = AmyShop.objects.filter(name__contains=prd)
    # print(shop)
    context = {
        'data' : shop
    }
    return render(request, 'secondapp/showArmyShop.html', context)

def showArmyShop2(request, year, month):
    course = AmyShop.objects.filter(year=year, month=month)
    print(course)
    context = {
        'data' : course
    }
    return render(request, 'secondapp/showArmyShop.html', context)

    
def req_ajax_exam(request):
    return render(request, 'secondapp/ajax_exam.html')

from django.forms.models import model_to_dict
def req_ajax_get(request):
    print("req_ajax_get")
    name = request.GET.get('name')
    # print("name:", name)
    if len(name) > 0:
        co = Course.objects.filter(name__contains=name)
    else:
        co = Course.objects.all()
    c_list = []
    for c in co:
            c = model_to_dict(c)
            c_list.append(c)
    
    return HttpResponse(c_list)

def req_ajax_post(request):
    print("req_ajax_post")
    name = request.POST.get('name')
    # print("name:", type(name))
    # co = Course.objects.all()
    if name is None:
        co = Course.objects.all()
    else:
        co = Course.objects.filter(name__contains=name)
    c_list = []
    for c in co:
            c = model_to_dict(c)
            c_list.append(c)

    return HttpResponse(c_list)

import json
def req_ajax_json(request):
    obj = request.body.decode("utf-8")
    data = json.loads(obj)

    co = Course.objects.all()
    c_list = []
    for c in co:
            c = model_to_dict(c)
            c_list.append(c)
    
    return JsonResponse(c_list, safe=False)

from .forms import CourseForm
def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('secondapp:show')
    else:
        form = CourseForm()
    return render(
        request, 'secondapp/course_create.html',
        {'form': form}
    )


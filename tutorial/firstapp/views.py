from django.http.response import JsonResponse
from django.shortcuts import redirect, render

# Create your views here.
# 두뇌, controller

from django.http import HttpResponse

def index1(request): # request 파라미터 필수
    # do something....
    return HttpResponse('<u>Hello</u>')

def index2(request): # request 파라미터 필수
    # do something....
    return HttpResponse('<u>Hi</u>')

def main(request): # request 파라미터 필수
    # do something....
    return HttpResponse('<u>main</u>')

from .models import Curriculum
def insert(request): # request 파라미터 필수
    # 방식1
    # insert into curriculum values ('linux')
    Curriculum.objects.create(name='linux') # 데이터 입력

    # 방식2
    c = Curriculum(name='python') # 클래스 생성
    c.save()
    # 3-html/css/js 입력
    Curriculum(name='python').save()
    # 4-django 입력
    Curriculum(name='django').save()
    
    return HttpResponse('insert')

def show(request):
    curriculum = Curriculum.objects.all()
    print(curriculum)
    context = {
        'data' : curriculum
    } # Dictionalry
    return render(request, 'firstapp/show.html', context)
    # result = ''
    # for c in curriculum:
    #     result += c.name + '<br>'
    # return HttpResponse(result)


def req_get(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    c = request.GET.get('c')
    # c = request.GET['c'] # get() 에러 없음
    #                      # GET['c'] 에러가 날 수 있음
    result = '%s %s %s' % (a, b, c)
    return HttpResponse(result)

def req_post(request):
    if request.method == 'POST':
        a = request.POST.get('a')
        b = request.POST.get('b')
        c = request.POST['c']
        result = '%s %s %s' % (a, b, c)
        return HttpResponse(result)
    return render(request, 'firstapp/post.html')


def req_ajax1(request):
    return render(request, 'firstapp/ajax1.html')

def req_ajax2(request):
    return render(request, 'firstapp/ajax2.html')


import json
from django.forms.models import model_to_dict
def req_json(request):
    obj = request.body.decode("utf-8")
    data = json.loads(obj)

    # Curriculum 데이터를 JSON으로 응답
    # 1. 데이터 조회
    cur = Curriculum.objects.all()
    # QuerySet 이상한 형태 dict X, list X, 기본 자료형 X
    
    # 2. JSON 응답을 위한 형태로 변경
    c_list = []
    for c in cur:
            c = model_to_dict(c)
            c_list.append(c)
    
    return JsonResponse(c_list, safe=False)

def req_ajax4(request):
    return render(request, 'firstapp/ajax4.html')

def static(request):
    return render(request, 'firstapp/static.html')

def var(request):
    data = {
        'str': 'text', 'num': 10,
        'list': [1, 2, 3],
        'dict': {'a': 'aaa', 'b': 'bbb'}
    }
    return render(request, 'firstapp/var.html', data)

from secondapp.models import AmyShop
def tag(request):

    shops = AmyShop.objects.all()[:10] # 10개만 가져옴

    persons = [
        { 'num': 1, 'name': 'Park', 'score': 100 },
        { 'num': 2, 'name': 'Choi', 'score': 70 },
        { 'num': 3, 'name': 'Kim', 'score': 80 }
    ]
    animals = ['Cat', 'Dog']
    context = {
        'persons': persons,
        'animals': animals,
        'shops' : shops
    }
    return render(
        request, 'firstapp/tag.html', context)

def custom_filter(request):
    context = { 'price': 39800.5 }
    return render(
    request, 'firstapp/custom_filter.html', context)

def template(request):
    return render(
    request, 'firstapp/template.html')


from .forms import NameForm
def form_basic(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
    else:
        form = NameForm()
    return render(
        request, 'firstapp/form_basic.html',
        { 'form': form }
    )

from .forms import CurriculumForm
def form_model(request):
    if request.method == 'POST':
        form = CurriculumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/first/form/model/')
    else:
        form = CurriculumForm()
    return render(
        request, 'firstapp/form_model.html',
        {'form': form}
    )

from django.shortcuts import render

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

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
    course = AmyShop.objects.all()
    print(course)
    context = {
        'data' : course
    }
    return render(request, 'secondapp/showArmyShop.html', context)

from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import render

def index(request): # request 파라미터 필수
    # do something....
    # return HttpResponse('<u>View</u>')
    return render(request, 'index.html')

def home(request): # request 파라미터 필수
    # do something....
    return HttpResponse('<u>View</u>')

# JSON 1개 짜리
def dict(request): 
    # do something....
    return JsonResponse({
        'key' : 'value',
        'key2' : 'value2'
    })

# JSON 여러개 짜리
def list(request):
    # do something....
    return JsonResponse(
        [
            { 'key' : 'value' },
            { 'key2' : 'value2'}
        ], safe=False # dictionary 형태가 아닌 list와 같은 형태 사용디 반드시 safe=False
    )


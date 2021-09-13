from django.http import HttpResponse

def home(request): # request 파라미터 필수
    # do something....
    return HttpResponse('<u>View</u>')
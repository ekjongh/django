from django.shortcuts import render
from django.http.response import JsonResponse
import pickle
import os

# Create your views here.
# from .models import AmyShop
def main(request):
    return render(request, 'article/main.html', {})

def predict(request):

    # print("현재디렉토리", os.getcwd())
    with open("article/model.pkl", "rb") as file:
        model = pickle.load(file)

    result = {"code": 200}
    result["category"] = ["정치", "경제", "사회", "생활/문화", "세계", "IT/과학"]
    
    sentence = request.GET.get("sentence")
    pred = model.predict([sentence])[0] # pred : 105
    result["pred"] = result["category"][pred - 100]
    
    print({ 'pred' : result["pred"]})

    return JsonResponse({ 'pred' : result["pred"]})

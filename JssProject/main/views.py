from django.shortcuts import render, redirect
from .forms import JssForm
from .models import Jasoseol
# Create your views here.
def index(request):
    all_jss = Jasoseol.objects.all()
    return render(request, 'index.html', {'all_jss' : all_jss})

def create(request):
    #POST에 관련한 함수도 create에서 다 처리를 하고 싶기 때문에 여기다 추가
    if request.method == "POST":
        #받아온 객체들을 기반으로 filled_form이라는 변수에 모델폼에 넣을 것
        #POST 방식으로 넘어온 객체들이 자기소개서 폼에 넣어짐
        filled_form = JssForm(request.POST)
        #is_valid라는 함수는 들어온 데이터가 문제가 없는지 확인 후 문제가 없다면 다음으로 넘어감
        if filled_form.is_valid(): 
            filled_form.save()
            return redirect('index')
    jss_form = JssForm()
    return render(request, 'create.html', {'jss_form' : jss_form})
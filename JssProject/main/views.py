from django.shortcuts import render, redirect, get_object_or_404
from .forms import JssForm
from .models import Jasoseol
from django.http import Http404
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

def detail(request, jss_id):
    # try:
    #     my_jss = Jasoseol.objects.get(pk=jss_id)
    # except:
    #     raise Http404
    my_jss = get_object_or_404(Jasoseol, pk=jss_id)
    return render(request, 'detail.html', {'my_jss' : my_jss})

def delete(reqeust, jss_id):
    my_jss =Jasoseol.objects.get(pk=jss_id)
    my_jss.delete()
    return redirect('index')

def update(request, jss_id):
    my_jss =Jasoseol.objects.get(pk=jss_id)
    #modelform을 사용하겠다고 선언
    jss_form = JssForm(instance=my_jss)
    if request.method == "POST":
        updated_form = JssForm(request.POST, instance=my_jss)
        if updated_form.is_valid():
            updated_form.save()
            return redirect('index')
    return render(request, 'create.html', {'jss_form' : jss_form})
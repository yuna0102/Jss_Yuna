from django.shortcuts import render, redirect, get_object_or_404
from .forms import JssForm
from .models import Jasoseol
from django.http import Http404
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    #all_jss는 '모든' user가 쓴 글에 관한 정보
    all_jss = Jasoseol.objects.all()
    return render(request, 'index.html', {'all_jss' : all_jss})

def my_index(request):
    my_jss = Jasoseol.objects.filter(author=request.user)
    return render(request, 'index.html', {'all_jss' : my_jss})

@login_required(login_url='/login/')
def create(request):
    #POST에 관련한 함수도 create에서 다 처리를 하고 싶기 때문에 여기다 추가
    if request.method == "POST":
        #받아온 객체들을 기반으로 filled_form이라는 변수에 모델폼에 넣을 것
        #POST 방식으로 넘어온 객체들이 자기소개서 폼에 넣어짐
        filled_form = JssForm(request.POST)
        #is_valid라는 함수는 들어온 데이터가 문제가 없는지 확인 후 문제가 없다면 다음으로 넘어감
        if filled_form.is_valid(): 
            #임시 form 생성
            #commit 이라는 속성은 잠깐 코드를 지연시키고 그 안에서 원하는 행위들을 해줄 수 있음
            temp_form = filled_form.save(commit=False)
            temp_form.author = request.user
            filled_form.save()
            return redirect('index')
    jss_form = JssForm()
    return render(request, 'create.html', {'jss_form' : jss_form})

@login_required(login_url='/login/')
def detail(request, jss_id):
    # try:
    #     my_jss = Jasoseol.objects.get(pk=jss_id)
    # except:
    #     raise Http404
    my_jss = get_object_or_404(Jasoseol, pk=jss_id)
    return render(request, 'detail.html', {'my_jss' : my_jss})

def delete(reqeust, jss_id):
    #my_jss는 '특정'유저가 쓴 글에 관한 정보
    my_jss = Jasoseol.objects.get(pk=jss_id)
    if reqeust.user == my_jss.author :
        my_jss.delete()
        return redirect('index')

    raise PermissionDenied
    
    
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
from django import forms
from .models import Jasoseol

class JssForm(forms.ModelForm):

    class Meta:
        model = Jasoseol
        fields = ('title', 'content')
    
    def __init__(self, *args, **kwargs):
        #super라는 것은 부모 클래스의 요소를 가져올 수 있는 것임
        #지금은 super의 부모요소가 modelform이기 때문에 modelform안의 __init__이라는 기능을 가져올 것임
        super().__init__(*args, **kwargs)
        #modelform은 기존에 있는 것을 활용하는 것이기 때문에 model에 있는 object의 이름으로 label이 달림.
        #제목을 바꾸기 위해서는 아래와 같은 함수를 사용해서 우변에 바꾸고자 하는 label 이름을 적으면 됨
        self.fields['title'].label = "제목"
        self.fields['content'].label = "자기소개서 내용"
        self.fields['title'].widget.attrs.update({
            'class' : 'jss_title',
            'placeholder' : '제목',
        })
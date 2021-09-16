
from django import forms
from .models import Course
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'cnt'] # id 속성은 PK 이므로 사용하지 않음
        widgets = { # fields에 명시된 속성만 사용
            'name': forms.TextInput(
            attrs={'required': False, 'size': 30}),
            'cnt': forms.TextInput(
            attrs={'required': False, 'size': 10}),
        }
        labels = { # fields에 명시된 속성만 사용
           'name': '과목',
           'cnt' : '인원수'
        }
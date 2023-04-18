from django import forms
from .models import First,Second,Third,Fourth,Fifth,Sixth,Seventh,Eighth,Title,Odai,Content,Follow,Good
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm


class OdaiForm(forms.ModelForm):
    class Meta:
        model = Odai
        fields = ('odai',)
        labels = {
            'odai':'タイトル入力',

        }

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ('content',)
        labels = {
            'content' : 'ゲーム内容を入力してください．',
        }

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    pass


class FindUserForm(forms.Form):
    username = forms.CharField(label='ユーザ',required=False)


class UserForm(forms.Form):
    user = forms.CharField(label='ユーザ',required=False)

class FollowForm(forms.Form):
    def __init__(self,user,*args,**kwargs):
        super(FollowForm,self).__init__(*args,**kwargs)
        self.fields['friends'] = forms.MultipleChoiceField(
            choices=[(item.user,item.user) for item in friends],
            widget=forms.CheckboxSelectMultiple(),
            initial=vals
        )
    
class GoodForm(forms.ModelForm):
    class Meta:
        model = Good
        fields = ['user','good']
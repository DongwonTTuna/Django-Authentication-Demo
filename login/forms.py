from django import forms
from PIL import Image
from io import BytesIO
from django.core.files import File


class LoginIDForm(forms.Form):
    u_id = forms.CharField(label="会員ID" , label_suffix='' ,max_length=255, required=True)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        
        self.fields['u_id'].widget.attrs['class'] = 'rounded-md mt-2 w-56 px-4 h-10 bg-[rgba(255,255,255,0.5)] '
        self.fields['u_id'].widget.attrs['placeholder'] = 'ID'

    

        
class LoginPWForm(forms.Form):
    password = forms.CharField(label="パスワード",label_suffix='' ,max_length=255, required=True, widget=forms.PasswordInput())
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['password'].widget.attrs['class'] = 'rounded-md mt-2 w-56 px-4 h-10 bg-[rgba(255,255,255,0.5)] '
        self.fields['password'].widget.attrs['placeholder'] = 'パスワード'


class RegisterForm(forms.Form):

    email = forms.EmailField(label='Eメール')
    password = forms.CharField(label="パスワード", label_suffix='',max_length=255, required=True,widget=forms.PasswordInput())
    name = forms.CharField(label='名前', max_length=30)
    address = forms.CharField(label='住所', max_length=100)
    profile_img = forms.ImageField(label='Profile Image')
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['email'].widget.attrs['class'] = 'rounded-md mt-2 w-56 px-4 h-10 bg-[rgba(255,255,255,0.5)] '
        self.fields['email'].widget.attrs['placeholder'] = 'メールアドレスを入力'
        
        self.fields['password'].widget.attrs['class'] = 'rounded-md mt-2 w-56 px-4 h-10 bg-[rgba(255,255,255,0.5)] '
        self.fields['password'].widget.attrs['placeholder'] = 'パスワードを入力'
        
        self.fields['name'].widget.attrs['class'] = 'rounded-md mt-2 w-56 px-4 h-10 bg-[rgba(255,255,255,0.5)] '
        self.fields['name'].widget.attrs['placeholder'] = '名前を入力'
        
        self.fields['address'].widget.attrs['class'] = 'rounded-md mt-2 w-56 px-4 h-10 bg-[rgba(255,255,255,0.5)] '
        self.fields['address'].widget.attrs['placeholder'] = '住所を入力'
        
        self.fields['profile_img'].widget.attrs['class'] = 'rounded-md mt-2 w-56 px-4 h-10 bg-[rgba(255,255,255,0.5)] '
from django import forms


class LoginIDForm(forms.Form):
    u_id = forms.CharField(label="会員ID" , label_suffix='' ,max_length=255, required=True)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        
        self.fields['u_id'].widget.attrs['class'] = 'rounded-md mt-2 w-56 px-4 h-10 bg-[rgba(255,255,255,0.5)] '
        self.fields['u_id'].widget.attrs['placeholder'] = 'ID'

    

        
class LoginPWForm(forms.Form):
    password = forms.CharField(label="パスワード",label_suffix='' ,max_length=255, required=True)
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['password'].widget.attrs['class'] = 'rounded-md mt-2 w-56 px-4 h-10 bg-[rgba(255,255,255,0.5)] '
        self.fields['password'].widget.attrs['placeholder'] = 'パスワード'
class RegisterForm(forms.Form):
    name = forms.CharField(label='名前', max_length=30)
    age = forms.IntegerField(label='年齢')
    telenum = forms.CharField(label='電話番号', max_length=11)
    email = forms.EmailField(label='Mail')
    address = forms.CharField(label='住所', max_length=100)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = '名前を入力'

        self.fields['age'].widget.attrs['class'] = 'form-control'
        self.fields['age'].widget.attrs['placeholder'] = '年齢を入力'
        
        self.fields['telenum'].widget.attrs['class'] = 'form-control'
        self.fields['telenum'].widget.attrs['placeholder'] = '電話番号を入力'

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'メールアドレスを入力'
        
        self.fields['address'].widget.attrs['class'] = 'form-control'
        self.fields['address'].widget.attrs['placeholder'] = '住所を入力'
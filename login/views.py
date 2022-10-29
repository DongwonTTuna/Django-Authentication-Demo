from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .forms import *
from .models import CustomUser
from urllib.parse import urlencode
import psycopg,brotli, base64
# Create your views here.


class LoginIDView(generic.FormView):
    template_name: str = "loginid.html"
    form_class = LoginIDForm
    def form_valid (self, form):
        self.form = form
        return HttpResponseRedirect(self.get_success_url())
    def get_success_url(self):
        u_id = self.form.cleaned_data['u_id']
        return "".join([reverse('loginpw'),'?',urlencode(dict(u_id=u_id))])

class LoginPWView(generic.FormView):
    template_name: str = 'loginpw.html'
    form_class = LoginPWForm
    
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)
        user = self.request.GET.get('u_id')
        data = CustomUser(user_email=user)
        with open('./resdata.txt','w') as f:
            f.write(str(data.objects.all()))
        #data = base64.b64encode(brotli.decompress(tempdata[0][0]))
        
        ctx.update(data)
        return ctx 
    
    
class RegisterView(generic.FormView):
    template_name: str = 'signup.html'
    form_class = RegisterForm
    
    def valid_extension(self,_img):
        if '.jpg' in _img:
            return "JPEG"
        elif '.jpeg' in _img:
            return 'JPEG'
        elif '.png' in _img:
            return 'PNG'
    def compress_image(self, image):
        im = Image.open(image)
        im = im.resize((250,250), Image.ANTIALIAS)
        im_io = BytesIO()
        extension = self.valid_extension(image.name)
        im.save(im_io, extension, optimize=True)
        new_image = File(im_io, name="UserProfileImg."+extension.lower())
        return new_image
    
    def form_valid(self,form):
        self.form = form
        email = self.form.cleaned_data['email']
        password = self.form.cleaned_data['password']
        name = self.form.cleaned_data['name']
        address = self.form.cleaned_data['address']
        img = self.compress_image(self.form.cleaned_data['profile_img'])
        data = CustomUser(user_email=email, u_password=password,name=name,user_address=address,user_profile_img=img)
        data.save()
        return HttpResponseRedirect(reverse('marketmain'))
           
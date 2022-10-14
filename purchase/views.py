from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .forms import *
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
        with psycopg.connect('dbname=purchase user=postgres password=0790') as post:
            with post.cursor() as cur:
                cur.execute('SELECT user_profile_img from USERS where user_id = %s',(self.request.GET.get('u_id'),))
                tempdata = cur.fetchall()
                if len(tempdata) == 0:
                    data = {'imgsrc': None}
                    ctx.update(data)
                    return ctx
                data = base64.b64encode(brotli.decompress(tempdata[0][0]))
                data = {"imgsrc": data.decode()}
                ctx.update(data)
        return ctx 
    
    
    

class Register(generic.FormView):
    template_name: str = 'register.html'
    form_clas = RegisterForm

class MarketView(generic.TemplateView):
    template_name: str = "market.html"
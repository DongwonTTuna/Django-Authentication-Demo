from django.views import generic

# Create your views here.

class MarketView(generic.TemplateView):
    
    template_name: str = "market.html"
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)
        user = self.request.session['login']
        if user == None:
            return ctx
        user_email = self.request.session['u_id']
        ctx.update({'u_id': str(user_email)})
        return ctx
    
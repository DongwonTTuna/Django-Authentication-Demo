from django.views import generic

# Create your views here.

class MarketView(generic.TemplateView):
    template_name: str = "market.html"
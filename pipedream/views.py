from django.http import HttpResponse
from pipedream.models import *
# Create your views here.
from django.template import RequestContext, loader


def home(request):
    interfaces = Interface.objects.all()
    template = loader.get_template('pipedream/index.html')
    context = RequestContext(request, {
        'interfaces': interfaces,
    })
    return HttpResponse(template.render(context))
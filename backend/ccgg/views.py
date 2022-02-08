
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('ccgg/index.html')
    context = {'fake': 1}
    return HttpResponse(template.render(context, request))

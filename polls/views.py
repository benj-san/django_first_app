from django.shortcuts import get_object_or_404, render

# Create your views here.

from django.http import HttpResponse
from django.template import loader

from .models import Protagonist


def index(request):
    first_heroes = Protagonist.objects.order_by('id')

    # Classic output with no html render
    # output = ", ".join([p.protagonist_name for p in first_heroes])
    # return HttpResponse(output)

    # A classic way to render
    # template = loader.get_template('index.html')
    context = {
        'first_heroes': first_heroes
    }
    # return HttpResponse(template.render(context, request))

    # A shorter way to render
    return render(request, 'protagonists/index.html', context)


def show(request, protagonist_id):
    # response = "Hero number %s is right here"
    # return HttpResponse(response % protagonist_id)
    protagonist = get_object_or_404(Protagonist, pk=protagonist_id)
    return render(request, 'protagonists/detail.html', {'protagonist': protagonist})

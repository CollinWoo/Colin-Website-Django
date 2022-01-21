from django.shortcuts import render
from .models import ProjectCard

# Create your views here.
def index(request):
    card_list = ProjectCard.objects.order_by('order')[:6]
    context = {
        'card_list': card_list,
    }
    
    return render(request, 'index.html', context)

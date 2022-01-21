from django.shortcuts import render, get_object_or_404
from .models import *
from markdown import markdown

# Create your views here.
def index(request):
    card_list = ProjectCard.objects.order_by('order')[:6]
    context = {
        'card_list': card_list,
    }
    
    return render(request, 'index.html', context)

def carddesc(request, slug):
    card = get_object_or_404(DescriptionPage, slug = slug)
    text = markdown(card.content, extensions=['tables','footnotes','mdx_linkify'])
    context = {
        'card': card,
        'text': text,
    }

    return render(request, 'post.html', context)

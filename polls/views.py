from django.shortcuts import render
from django.http import HttpResponse# Create your views here.
from django.utils.html import mark_safe
from .models import Question
from django.shortcuts import get_object_or_404


def index(request):
    return render(request, 'polls/index.html', {
        'questions': Question.objects.all(),
    })

def detail(request, pk):
    obj = get_object_or_404(Question, pk=pk)
    return render(request, 'polls/detail.html', {
        'question': obj,
    })

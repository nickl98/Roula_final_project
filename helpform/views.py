from django.shortcuts import render

# Create your views here.
from .models import Question

# coach logic and return of view


def question(request):
    """function to render Devloper on page"""
    questions = Question.objects.all()

    context = {
        'questions': questions,
    }
    return render(request, 'questions/question.html', context)


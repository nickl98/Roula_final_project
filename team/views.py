from django.shortcuts import render
from .models import Team

# coach logic and return of view


def team(request):
    """function to render coaches on page"""
    teams = Team.objects.all()

    context = {
        'teams': teams,
    }
    return render(request, 'teams/team.html', context)

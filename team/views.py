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


def dev_detail(request):
    """ A view to show individual product details """

    
    context = {
        'team': team,
    }

    return render(request, 'team/view_dev.html', context)

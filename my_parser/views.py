from django.shortcuts import render
import requests
from ..scrapFree import habr_parsing


def index(request):
    jobs = habr_parsing('https://freelance.habr.com/tasks?q=python&categories=development_all_inclusive,development_backend,development_frontend,development_prototyping,development_ios,development_android,development_desktop,development_bots,development_games,development_1c_dev,development_scripts,development_voice_interfaces,development_other')
    return render(request, 'index.html', {'jobs': jobs})

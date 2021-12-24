from django.http.response import HttpResponse
from django.views import View
from jobs.models import Followers
from scrapFree import habr_parsing
from django.shortcuts import redirect, render


class HomePageView(View):
    def get(self, request):
        jobs = habr_parsing('''https://freelance.habr.com/tasks?q=python&
        categories=development_all_inclusive,development_backend,development_
        frontend,development_prototyping,development_ios,development_android,
        development_desktop,development_bots,development_games,development_1c
        _dev,development_scripts,development_voice_interfaces,development_
        other''')
        return render(request, 'index.html', {'jobs': jobs})

    def post(self, request):
        email = request.POST.get('email')
        f = Followers.objects.filter(email=email)
        if f:
            return HttpResponse('Такой email уже существует')
        if email:
            f = Followers(email=email)
            f.save()
        return redirect('index')

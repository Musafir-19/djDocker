import os
import sys
from bs4 import BeautifulSoup as BS
import requests
from django.db import DatabaseError


proj = os.path.dirname(os.path.abspath('manage.py'))

sys.path.append(proj)

os.environ['DJANGO_SETTINGS_MODULE'] = 'iFreeLancer.settings'

import django 

django.setup()

from jobs.models import Job


url = 'https://freelance.habr.com/tasks?q=python&categories=development_all_inclusive,development_backend,development_frontend,development_prototyping,development_ios,development_android,development_desktop,development_bots,development_games,development_1c_dev,development_scripts,development_voice_interfaces,development_other'


def habr_parsing():
    url = 'https://freelance.habr.com/tasks?q=python&categories=development_all_inclusive,development_backend,development_frontend,development_prototyping,development_ios,development_android,development_desktop,development_bots,development_games,development_1c_dev,development_scripts,development_voice_interfaces,development_other'
    jobs = []
    res = requests.get(url)
    if res.status_code == 200:
        soup = BS(res.content, 'html.parser')
        ul = soup.find('ul', id='tasks_list')
        li = ul.find_all('li', class_='content-list__item')
        for i in li:
            url = 'https://freelance.habr.com/' + i.a['href']
            title = i.a.text
            price = 'договорная'
            responses = '0 просмотров'
            if i.find('span', class_='count'):
                price = i.find('span', class_='count').text
            views = i.find(
                'span', class_='params__views icon_task_views').text.strip()
            if i.find('span', class_='icon_task_responses'):
                responses = i.find(
                    'span', class_='icon_task_responses').text.strip()
            time = i.find('span', class_='icon_task_publish_at').text.strip()
            jobs.append({'url': url, 'title': title, 'price': price,
                        'views': views, 'responses': responses, 'time': time})
    return jobs

def save_jobs():
    habr_jobs = habr_parsing()
    for job in habr_jobs:
        j = Job(**job)
        try:
            j.save()
        except DatabaseError:
            pass


if __name__ == '__main__':
    save_jobs()

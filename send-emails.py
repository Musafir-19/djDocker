import os
import sys
from datetime import datetime
from bs4 import BeautifulSoup as BS
import requests
from django.db import DatabaseError


proj = os.path.dirname(os.path.abspath('manage.py'))

sys.path.append(proj)

os.environ['DJANGO_SETTINGS_MODULE'] = 'iFreeLancer.settings'

import django 
django.setup()

from django.core.mail import EmailMultiAlternatives
from iFreeLancer.settings import EMAIL_HOST_USER
from jobs.models import Followers
from scrapFree import habr_parsing

jobs = habr_parsing()
emails = Followers.objects.all()
subject = f'Заказы для Вас на сегодня {datetime.today()}'
from_email = EMAIL_HOST_USER
text_content = 'Рассылка заказов.'
html_content = ''
for email in emails:
    for job in jobs:  
        html_content += f'''<h5 class="card-title">{ job.get('title') }</h5>
                <p class="card-text">{ job.get('responses') } | 
                { job.get('views') } |
                { job.get('time') }</p>
                <a href="{ job.get('url') }" 
                class="btn btn-primary">Перейти к заказу</a>
                <h6 class="card-title">{  job.get('price') }</h6>'''
        msg = EmailMultiAlternatives(subject, text_content, from_email, [email])
        msg.attach_alternative(html_content, 'text/html')
        msg.send() 
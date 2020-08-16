import requests

from django.core.management import BaseCommand
from apscheduler.schedulers.blocking import BlockingScheduler
from django.core.mail import send_mass_mail, EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from subscribe.models import Subscribe
from bs4 import BeautifulSoup

data = {}

for rows in BeautifulSoup(requests.get("https://www.worldometers.info/coronavirus/").text,
                          'html.parser').find(
    'div', class_="main_table_countries_div").find('tbody').find_all('tr')[8:]:
    sub_data = []
    for row_data in rows.find_all('td'):
        sub_data.append(row_data.text)
    sub_data = sub_data[1:-4]
    dict_sub_data = {
        'country': sub_data[0],
        'total_cases': sub_data[1],
        'new_cases': sub_data[2][1:],
        'total_deaths': sub_data[3],
        'new_deaths': sub_data[4][1:],
        'total_recovered': sub_data[5],
        'new_recovered': sub_data[6][1:],
        'active_cases': sub_data[7],
        'critical_cases': sub_data[8],
        'total_test': sub_data[11],
        'population': sub_data[13]
    }

    # checking if None
    if not dict_sub_data['new_cases']:
        dict_sub_data['new_cases'] = 'None'
    if not dict_sub_data['new_deaths']:
        dict_sub_data['new_deaths'] = 'None'
    if not dict_sub_data['new_recovered']:
        dict_sub_data['new_recovered'] = 'None'

    data[list(dict_sub_data.values())[0].upper()] = dict_sub_data


def send_html_email(to_list, subject, template_name, context, sender=settings.DEFAULT_FROM_EMAIL):
    msg_html = render_to_string(template_name, context)
    msg = EmailMessage(subject=subject, body=msg_html, from_email=sender, bcc=to_list)
    msg.content_subtype = "html"  # Main content is now text/html
    return msg.send()


def send_to_subscribers():
    for subscriber in Subscribe.objects.all():
        dt_country = subscriber.country.upper()
        context = {
            'country': data[dt_country]['country'].capitalize(),
            'total_cases': data[dt_country]['total_cases'],
            'total_deaths': data[dt_country]['total_deaths'],
            'new_cases': data[dt_country]['new_cases'],
            'active_cases': data[dt_country]['active_cases'],
            'new_recovered': data[dt_country]['new_recovered'],
            'critical_condition': data[dt_country]['critical_cases'],
            'new_deaths': data[dt_country]['new_deaths']
        }

        send_html_email((subscriber.email,), f'CoronavirusData: {subscriber.country.capitalize()}',
                        'subscribe/email.html', context, "testkenny00@gmail.com")


class Command(BaseCommand):
    help = """Scrapes data from 'https://www.worldometers.info/coronavirus/' 
    and then sends the data to the subscriber based on their country"""

    def handle(self, *args, **options):
        sched = BlockingScheduler()
        sched.add_job(send_to_subscribers, 'interval', minutes=25)
        sched.start()

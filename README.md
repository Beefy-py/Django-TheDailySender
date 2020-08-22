# Django-TheDailySender
Not really a daily sender but it sends you Corona virus stats from a country of your choosing.

![Image of what the subscribe page looks like](https://github.com/Beefy-py/Django-TheDailySender/blob/master/subscribe/static/subscribe/images/Capture.PNG)

**Live demo:[TheDailySender](https://the-daily-sender.herokuapp.com/)** 

## Setup
Go in the directory where `manage.py` is located and enter
`pipenv install requirements.txt` or `pip install requirements.txt`

## Know Problems

1. I have a hobby heroku server so it only runs for 30 minutes then closes.
2. That "send_daily" command should actually send an email every twelve hours. But because my server only stays on for 30 minutes, it will send an email in 25 minutes and then no more until someone goes back to my website.

## Todo
In the *unsubscribe* page you can just remove any email. Not just yours😅. So i gotta fix that.

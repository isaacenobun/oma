from django.core.mail import send_mail
import datetime
from .mails import all_mails
    
def send_oma_mail():
    start_date = datetime.date(2025, 2, 22)
    
    today = datetime.date.today()
    
    diff = (today - start_date).days
    
    mail = all_mails[diff]

    for items in mail.items():
        texts = items[1]
        for key,value in texts.items():
            subject = key
            body = value
    
    send_mail(
        subject,
        body,
        'isaacenobun@gmail.com',
        ['isaacenobun@gmail.com'],
    )
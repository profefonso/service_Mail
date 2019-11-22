from simit_services.celery import app

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def asinc_mail(list_emails=[], subject='NO SUBJECT', template=None, content_data=None):
    sender = "TORES BALON <infomercadigital@gmail.com>"

    merge_data = content_data
    text_body = render_to_string("../templates/"+template+".txt", merge_data)
    html_body = render_to_string("../templates/"+template+".html", merge_data)

    msg = EmailMultiAlternatives(subject=subject, from_email=sender,
                                 to=list_emails, body=text_body)
    msg.attach_alternative(html_body, "text/html")
    msg.send()

from django.conf import settings
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

def send_email_contact(name,email, subject, message):
    html_content = render_to_string('emails/confirm-contact.html', {"name":name, "subject":subject, "email":email, "message":message})
    text_content = strip_tags(html_content)
    
    prepared_email = EmailMultiAlternatives(subject=subject, body=text_content, from_email=settings.EMAIL_HOST_USER,to=['eriveltoclenio@gmail.com',])
    prepared_email.attach_alternative(html_content, 'text/html')
    prepared_email.send()
    return True

def send_email_confirm_newletters(person_email):
    subject = 'Confirmação de Subcrição da Newletter'
    list_emails = [person_email,]

    html_content = render_to_string('emails/confirm-newletters.html', {})
    text_content = strip_tags(html_content)
    
    email = EmailMultiAlternatives(subject=subject, body=text_content, from_email=settings.EMAIL_HOST_USER,to=list_emails)
    email.attach_alternative(html_content, 'text/html')
    email.send()
    return True
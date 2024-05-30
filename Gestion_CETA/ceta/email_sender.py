import os
from email.message import EmailMessage
import ssl
import smtplib

def send_mail(user_mail):
    emissor_mail,emissor_password,subject,content = email_config()
    email = build_email(user_mail, emissor_mail, subject, content)
    ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login(emissor_mail,emissor_password)
        smtp.sendmail(emissor_mail,user_mail,email.as_string())

def build_email(user_mail, emissor_mail, subject, content):
    email = EmailMessage()
    email['From'] = emissor_mail
    email['To'] = user_mail
    email['Subject'] = subject
    email.set_content(content)
    return email


def email_config():
    #password: 
    emissor_mail, emissor_password = ('cetacorreoprueba@gmail.com',os.environ.get('EMAIL_PASSWORD'))
    subject = 'Bienvenido a CETA'
    content = """
        Has sido registrado correctamente en la aplicación. Entre a este enlace: http://localhost:5137 para ingresar su usuario y contraseña satisfactoriamente
    """
    return emissor_mail,emissor_password,subject,content
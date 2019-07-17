import smtplib
import os


EMAIL = os.environ.get('EMAIL1')
PASSWD = os.environ.get('PASSWD1')
EMAIL2 = os.environ.get('EMAIL2')

print(EMAIL, PASSWD, EMAIL2)
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    #here i tell him to make connection
    smtp.ehlo()
    #i will encrypt my connection
    smtp.starttls()
    #then i tell him to reconnect as encrypted
    smtp.ehlo()
    smtp.login(EMAIL, PASSWD)

    subject = 'Yes it had worked'
    body = 'I want to tell you that it had succeeded'

    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(EMAIL, EMAIL2, msg)

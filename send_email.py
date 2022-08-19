import email
from email.mime.text import MIMEText
import smtplib


def send_email(name, email, phone, topic, level_en, weekday):
    from_email = "speaking.club.best@gmail.com"
    from_password="kbsmttcelnhalloe"
    to_email=email

    subject="Speaking club"
    message=f""" Hi, <strong>{name}</strong>! <br>
    You registration is success! <br>
    You have an excellent level of English.<br>
    We are waiting for you on {weekday} at 11:00. <br>
    Our manager will contact you within a day. <br><br> Good day!""" 

    msg=MIMEText(message, "html")
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    gmail=smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email,from_password)
    gmail.send_message(msg)

from email.message import EmailMessage
import ssl
import smtplib

EMAIL_PASS = "###"  # add your security key into here
EMAIL_SENDER = "###"  # their email

EMAIL_RECIEVER = "###"  # your email

subject = "Don't forget to add a subject!"

body = """
    Hey there , this email was sent from a python
    bot remember , you need to finish other python
    projects to get that job!


"""

em = EmailMessage()
em["From"] = EMAIL_SENDER
em["to"] = EMAIL_RECIEVER
em["subject"] = subject
em.set_content(body)


context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(EMAIL_SENDER, EMAIL_PASS)
    smtp.sendmail(EMAIL_SENDER, EMAIL_RECIEVER, em.as_string())

from email.message import EmailMessage
from passwordGoogle import password
import ssl
import smtplib

emailSender = "muhammadalishuhratjonov50@gmail.com"
emai_password = password

email_receiver = "muhammadalishuhratjonov92@gmail.com"

subject = "python developer"
body = """
hi, bro.
"""

em = EmailMessage()
em["from"] = emailSender
em["to"] = email_receiver
em["subject"] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as stmp:
    stmp.login(emailSender, emai_password)
    stmp.sendmail(emailSender, email_receiver, em.as_string())

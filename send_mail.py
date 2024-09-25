import smtplib
import ssl
import os


def send_mail(message):
    app_mail = "gunzeuxapp@gmail.com"
    password = os.getenv("GA_GEN_PASS")
    recipient_mail = "gunzeux71+app5@gmail.com"

    host = "smtp.gmail.com"
    port = 465
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
        server.login(app_mail, password)
        server.sendmail(app_mail, recipient_mail, message)
import smtplib
import os

HOST = os.environ['HOST_ENV']
PORT = os.environ['PORT_ENV']

FROM_EMAIL = os.environ['FROM_EMAIL_ENV']
TO_EMAIL = os.environ['TO_EMAIL_ENV']
PASSWORD = os.environ['PASSWORD_ENV']

MESSAGE = """Subject: Server Alert
Web App is running.
"""

smtp = smtplib.SMTP(HOST, PORT)

status_code, response = smtp.ehlo()
status_code, response = smtp.starttls()
status_code, response = smtp.login(FROM_EMAIL, PASSWORD)
smtp.sendmail(FROM_EMAIL, TO_EMAIL, MESSAGE)

smtp.quit()
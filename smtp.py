import smtplib

HOST = "mxslurp.click"
PORT = 2525

FROM_EMAIL = ""
TO_EMAIL = ""
#USERNAME = ""
PASSWORD = ""

MESSAGE = """Subject: Server Alert
Web App is running.
"""

smtp = smtplib.SMTP(HOST, PORT)

status_code, response = smtp.ehlo()
print(f"[*] Echoing the server: {status_code} {response}")

status_code, response = smtp.starttls()
print(f"[*] Starting TLS connection: {status_code} {response}")

status_code, response = smtp.login(FROM_EMAIL, PASSWORD)
print(f"[*] Logging: {status_code} {response}")

smtp.sendmail(FROM_EMAIL, TO_EMAIL, MESSAGE)

smtp.quit()  
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, to_email):
    smtp_server = 'smtp.yourmailserver.com'
    smtp_port = 587  # or 465 for SSL/TLS
    smtp_username = 'your_username'
    smtp_password = 'your_password'

    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.send_message(msg)
    server.quit()

# Example usage
send_email('Subject', 'Body', 'recipient@example.com')

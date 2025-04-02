import smtplib

def send_email(to, subject, body):
    server = smtplib.SMTP("smtp.example.com")
    message = f"Subject: {subject},{body}"
    server.sendmail("noreply@example.com", to, message)
    server.quit()
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, message, to_email, smtp_server, smtp_port, sender_email, sender_password):
    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = ', '.join(to_email)
    msg['Subject'] = subject

   
    msg.attach(MIMEText(message, 'plain'))

   
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        
        server.starttls()
        server.login(sender_email, sender_password)

       
        server.sendmail(sender_email, to_email, msg.as_string())


subject = "Test Email"
message = "This is a test email sent from Python."
to_email = ["sonusmj0112@gmail.com", "pritjoshi0112@gmail.com"]
smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = "dectmark01@gmail.com"
sender_password = "Sunnybhai1811"

send_email(subject, message, to_email, smtp_server, smtp_port, sender_email, sender_password)

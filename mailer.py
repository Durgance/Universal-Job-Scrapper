import ssl
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


smtp_server = "smtp.gmail.com" # for Gmail
port = 587  # For starttls

sender_email = ""  # email address used to generate password
receiver_email = [""] # a list of recipients 
password = "" # pwd from google to consider this application an app , find this in settings

def format_mail(data):
    msg = MIMEMultipart()
    msg["Subject"] = "Training Job Notification"
    msg["From"] = sender_email
    msg['To'] = ", ".join(receiver_email)
    text = f"Job Vaccancy in UBER link : {[_ for _ in data]}"
    body_text = MIMEText(text, 'plain')  
    msg.attach(body_text)  # attaching the text body into msg
    return msg

def send_mail(msg):
    context = ssl.create_default_context()
    # Try to log in to server and send email 
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()  # check connection
        server.starttls(context=context)  # Secure the connection
        server.ehlo()  # check connection
        server.login(sender_email, password)

        # Send email here
        server.sendmail(sender_email, receiver_email, msg.as_string())

    except Exception as e:
        # Print any error messages 
        print(e)
    finally:
        server.quit()

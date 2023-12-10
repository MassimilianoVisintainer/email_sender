from email.message import EmailMessage
from dotenv import load_dotenv
import os
import ssl
import smtplib

# Load environment variables from .env
load_dotenv()

# Access environment variables
email_sender = os.getenv("EMAIL_SENDER")
email_password = os.getenv("PASSWORD")
email_receiver = os.getenv("EMAIL_RECEIVER")

subject = "Don't miss this email"
body = """
Please read the detail here
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

# Create SSL Context for secure communication
context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.send_message(em)

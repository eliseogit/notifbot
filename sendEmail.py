import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from emails import EMAILS
import os

# Documentation incase adjustments or updates are needed.
# https://docs.python.org/3/library/email.mime.html

# Function to send email with attachment
def send_email(sender_email, sender_password, receiver_email, subject, body, attachment_path=None):
    # Set up the MIME
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Add the email body to the MIME message
    msg.attach(MIMEText(body, 'plain'))

    # Add the attachment if provided
    if attachment_path:
        try:
            # Open the file in binary mode
            with open(attachment_path, 'rb') as attachment:
                # Create a MIMEBase instance
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())

            # Encode the payload using Base64
            encoders.encode_base64(part)

            # Add header with the attachment file name
            part.add_header(
                'Content-Disposition',
                f'attachment; filename={os.path.basename(attachment_path)}'
            )

            # Attach the file to the message
            msg.attach(part)
        except Exception as e:
            print(f"Error attaching file: {e}")
            return

    try:
        # Create a secure SSL context and log in to the server
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, receiver_email, msg.as_string())

        # Quit the server connection
        server.quit()

        print("Email sent successfully to", receiver_email+"!")
    except Exception as e:
        print(f"Error: {e}")



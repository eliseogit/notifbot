import sendEmail
from emails import EMAILS
from creds import usernames
from creds import passwords

sender = "example1"
sender_email = usernames[sender]
sender_password = passwords[sender]
subject = "Example Subject"
body = """

Example sentence, example sentence, example sentence.

"""
###
# Put file path into "attachment_path"
# Most, if not all, file types are included.
# For more information check this google doc, https://support.google.com/drive/answer/37603?hl=en
# If it's not, complain to google (Sorry).
####
attachment_path = "/User/Path/Examplefile.pdf"  
for i in EMAILS.values():
    receiver_email = i
    sendEmail.send_email(sender_email, sender_password, receiver_email, subject, body, attachment_path)
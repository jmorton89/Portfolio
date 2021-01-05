from email.message import EmailMessage
import os.path
import mimetypes
import smtplib

message = EmailMessage()

sender = "example1@gmail.com"
recipient = "example2@gmail.com"
message['From'] = sender
message['To'] = recipient

message['Subject'] = 'Greetings from {} to {}!'.format(sender[0:4].upper(), recipient[0:7].upper())

body = """Hello
I hope your day is going well. I am sending this message to you using python instead of the gmail app!
See you later :) """
message.set_content(body)

attachment_path = "photo_path.jpg"
attachment = os.path.basename(attachment_path)
mime_type, _ = mimetypes.guess_type(attachment_path)
mime_type, mime_subtype = mime_type.split('/', 1)
with open(attachment_path, 'rb') as ap:
    message.add_attachment(ap.read(), maintype=mime_type,
    subtype=mime_subtype, filename=os.path.basename(attachment_path))

# print(message)

mail_server = smtplib.SMTP_SSL('smtp.gmail.com')
port = 465
# mail_server.set_debuglevel(1)
sender = 'example1@gmail.com'
password = 'password'
mail_server.login(sender, password)
mail_server.send_message(message)

# print(mail_server)
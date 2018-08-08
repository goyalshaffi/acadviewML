import sendgrid
import os
from sendgrid.helpers.mail import *

sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('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'))
from_email = Email("isha31198@gmail.com")
to_email = Email("megha.ahuja177@gmail.com")
subject = "tcdhhh"
content = Content("text/plain","seding msg")
mail = Mail(from_email, subject, to_email, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.body)
# ga naar gmail doe 2 factor auth aan
#genereer een app pasword in beveiligingsfuncties
#create a function to send the mail


from email.message import EmailMessage
#import  wachtwoord van een ander bestand; veiligheidsredenen
from appwdgoogle import password
import ssl
import smtplib

email_sender = ''
email_password = password
email_receiver = ''

subject = 'email onderwerp'
body = """
Dit is de tekst die in de email zit 
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

# specifieer de smtp server
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())



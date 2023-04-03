import requests
from math import floor
import time
import smtplib as smtp
from email.message import EmailMessage

book_url = 'https://www.gutenberg.org/files/2600/2600-0.txt'
r = requests.get(book_url)

book_data = r.text.encode('ascii', 'ignore').decode('ascii')

word_list = book_data.split(" ")

msg_size = floor(len(word_list) / 1000)
final_msg_size = len(word_list) - (msg_size * 999)

print(f"Words per message: {msg_size}\nFinal message size: {final_msg_size}")



#email login gegevens
##SMTP servers that I've used include:

#smtp.gmail.com (port 587)
#smtp.office365.com (port 587)
#smtp.mail.yahoo.com (port 587 or 465)



user = 'me@gmail.com'
password = 'p@ssword'
fr_adress = 'me@gmail.com'
to_adress = 'to@gmail.com,to2@gmail.com,to3@gmail.com' #moet een string zijn als je naar meerdere mensen wilt sturen
smtp_host = 'smtp.office365.com'
smtp_port = 587

subject = 'War & Peace part '
msg_text = ''
start_pos = 0
msg_count = 0

#server variabele en maakt de connectie
for b in range(20):

        server = smtp.SMTP(host=smtp_host, port=smtp_port)
        server.starttls()
        server.login(user=user, password=password)


        for i in range(50):
            if msg_count == 1000:
                start_pos = (len(word_list)-final_msg_size)
                msg_text = ' '.join(word_list[start_pos:])
            else:
                start_pos = msg_count * msg_size
                msg_text = ' '.join(word_list[start_pos:start_pos + msg_size])


        #email bericht maken
            msg = EmailMessage()
            msg['From'] = fr_adress
            msg['To'] = to_adress
            msg['Subject'] = subject + str(msg_count+1)
            msg.set_payload(msg_text)

            msg_count += 1


            server.send_message(msg)

            time.sleep(0.5)
            
        time.sleep(60)

        server.close()

    


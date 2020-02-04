# import necessary packages
 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
 
# create message object instance
msg = MIMEMultipart()
 
 
message = '''
Olá,

Esse é um e-mail de teste gerado via python!

Att,
Código
'''
 
# setup the parameters of the message
password = "---"
msg['From'] = "eqm@gmail.com"
msg['To'] = "---"
msg['Subject'] = "E-mail de teste"
 
# add in the message body
msg.attach(MIMEText(message, 'plain'))
 
#create server
server = smtplib.SMTP('smtp.gmail.com: 587')
 
server.starttls()
 
# Login Credentials for sending the mail
server.login(msg['From'], password)
 
 
# send the message via the server.
server.sendmail(msg['From'], msg['To'], msg.as_string())
 
server.quit()
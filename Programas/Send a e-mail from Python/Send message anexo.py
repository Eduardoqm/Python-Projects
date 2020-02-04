# send_attachment.py
# import necessary packages
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import email.mime.application
import smtplib
 
# create message object instance
msg = MIMEMultipart()
 
# setup the parameters of the message
password = "---"
msg['From'] = "eqm@gmail.com"
msg['To'] = "---"
msg['Subject'] = "E-mail de teste - Anexo"
 
# attach image to message body
body = MIMEText('''
Olá,

Segue em anexo!

Att,
EQM
''')
msg.attach(body)

file='C:/Users/Eduardo Q Marques/Documents/My Jobs/Programas/Python/Python-Projects/Programas/Send a e-mail from Python/logo.png'
fp=open(file,'rb')
anexo = email.mime.application.MIMEApplication(fp.read(),_subtype="png")
fp.close()
anexo.add_header('Content-Disposition','attachment',filename=file)
msg.attach(anexo)
 
 
# create server
server = smtplib.SMTP('smtp.gmail.com: 587')
 
server.starttls()
 
# Login Credentials for sending the mail
server.login(msg['From'], password)
 
 
# send the message via the server.
server.sendmail(msg['From'], msg['To'], msg.as_string())
 
server.quit()
import csv
import smtplib, ssl
from email.mime.text import MIMEText

port = 587
smtp = "smtp.gmail.com"
sender = ""
receiver = ""
password = ""

context = ssl.create_default_context()

server = smtplib.SMTP(smtp, port)

with open('FILENAME.csv') as file:
	reader = csv.reader(file, delimiter=',')
	count = 0
	server.starttls()
	for row in reader:
		if count >= 2:
			# print(row)
			
			name, email, number, date = row[1:5]
			print(name, email, number, date)
			receiver = email
			msg = MIMEText('')
			msg['From'] = ""
			msg['Subject'] = ""
			msg['To'] = email
			#
			server.ehlo()
			
			server.ehlo()
			
			server.login(sender, password)
			try:
				server.sendmail(sender, receiver, msg.as_string())
			except:
				print("ERROR:", receiver)
			# break
			
			
		count += 1
	

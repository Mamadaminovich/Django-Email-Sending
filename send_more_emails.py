import smtplib

# list of email_id to send the mail
li = ["yuriyboyka2209@gmail.com", "yuriyboyka2209@gmail.com", "yuriyboyka2209@gmail.com", "yuriyboyka2209@gmail.com"]

for dest in li:
	s = smtplib.SMTP('smtp.gmail.com', 587)
	s.starttls()
	s.login("mamadaminov001@gmail.com", "yxjg gbta qach wwei")
	message = "Assalomu Aleykum Multiply"
	s.sendmail("mamadaminov001@gmail.com", dest, message)
	s.quit()

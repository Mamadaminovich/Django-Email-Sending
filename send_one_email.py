import smtplib

s = smtplib.SMTP('smtp.gmail.com', 587)

s.starttls()

s.login("mamadaminov001@gmail.com", "yxjg gbta qach wwei")

message = "Assalomu Aleykum"

s.sendmail("mamadaminov001@gmail.com", "yuriyboyka2209@gmail.com", message)

s.quit()

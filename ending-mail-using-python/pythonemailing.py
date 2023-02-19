import smtplib
  
# creates SMTP session
session = smtplib.SMTP('smtp.gmail.com', 587)
  
# start TLS for security
session.starttls()
  
# Authentication
session.login("sender_email_id", "sender_email_id_password")
  
# message to be sent
message = "Message you want to send"
  
# sending the mail
session.sendmail("sender_email_id", "receiver_email_id", message)
  
# terminating the session
session.quit()

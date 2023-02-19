# My First Project
I recently dived into Python 3 as a learning exercise to explore how I could send a batch of emails. In a production setting, there may be more straightforward approaches, but the following worked well for me.

## Installation 
It is built-in module in python. No need of installation.

```python
import smtplib
smtpObj = smtplib.SMTP( [host [, port [, local_hostname]]] )
```
# Outline
* [SMTP](#smtp)
* [Algorithm](#algorithm)
* [Python Code](#python-code)

# Python : Sending Emails using SMTPLIB
I recently dived into Python 3 as a learning exercise to explore how I could send a batch of emails. In a production setting, there may be more straightforward approaches, but the following worked well for me.

So, let's say you have a list of contacts with their names and email addresses. And you'd like to send a message to each of those people, with the phrase "Dear [name]" at the head of the message.

You can save the contact information in a file rather than a database for ease of use. You can also save a file with the message template you want to send.

## SMTP
Simple Mail Transfer Protocol (SMTP) is a protocol, which handles sending e-mail and routing e-mail between mail servers.

Python provides smtplib module, which defines an SMTP client session object that can be used to send mail to any Internet machine with an SMTP or ESMTP listener daemon.

Here is a simple syntax to create one SMTP object, which can later be used to send an e-mail −

```python
import smtplib

smtpObj = smtplib.SMTP( [host [, port [, local_hostname]]] )
```
Here is the detail of the parameters −

1. host − This is the host running your SMTP server. You can specify IP address of the host or a domain name like tutorialspoint.com. This is optional argument.
2. port − If you are providing host argument, then you need to specify a port, where SMTP server is listening. Usually this port would be 25.
3. local_hostname − If your SMTP server is running on your local machine, then you can specify just localhost as of this option.

An SMTP object has an instance method called sendmail, which is typically used to do the work of mailing a message. It takes three parameters −

1. The sender − A string with the address of the sender.
2. The receivers − A list of strings, one for each recipient.
3. The message − A message as a string formatted as specified in the various RFCs.

## Algorithm

Here are four basic steps for sending emails using Python:

1. First and foremost, the "smtplib" library must be imported.

2. After that, we'll use its instance SMTP to wrap an SMTP connection to create a session. 

```python

s = smtplib.SMTP('smtp.gmail.com', 587)

```

You must pass the first parameter, which is the server's location, and the second value, which is the port to use. The port number 587 is used for Gmail. Different port numbers are used by different websites.

3. For security reasons, now put the SMTP connection in the TLS mode. TLS (Transport Layer Security) encrypts all the SMTP commands. After that, for security and authentication, you need to pass your Gmail account credentials in the login instance.The compiler will show an authentication error if you enter invalid email id or password.

4. Store the message you need to send in a variable say, message. Using the sendmail() instance, send your message. sendmail() uses three parameters: sender_email_id, receiver_email_id and message_to_be_sent. The parameters need to be in the same sequence.

5. After you have completed your task, terminate the SMTP session by using quit().    

## Python Code
       
```python
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
```
## NOTE :
This code can send simple mail which doesn’t have any attachment or any subject.

# Conclusion
This code can send plain text emails with no attachments or subject lines. 

Feel free to copy it and make changes as needed. 

Enjoy sending emails with Python, and don't forget to keep it spam-free!

# Contributing
Pull requests are welcome. For major changes, please open and issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

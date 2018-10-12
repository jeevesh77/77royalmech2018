import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
#Next, log in to the server
server.login("sco2jee@gmail.com", "9035265668")
#Send the mail
msg = "Hello!" # The /n separates the message from the headers
server.sendmail("sco2jee@gmail.com", "jeevanggowda51@gmail.com", msg)
server.quit()
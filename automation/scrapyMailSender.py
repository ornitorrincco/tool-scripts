from scrapy.mail import MailSender

def send_mail(self, message, title):
    print "Sending mail..........."
    import smtplib
    from email.MIMEMultipart import MIMEMultipart
    from email.MIMEText import MIMEText
    gmailUser = 'mail_you_send_from@gmail.com'
    gmailPassword = 'password'
    recipient = 'mail_to_send_to'

    msg = MIMEMultipart()
    msg['From'] = gmailUser
    msg['To'] = recipient
    msg['Subject'] = title
    msg.attach(MIMEText(message))

    mailServer = smtplib.SMTP('smtp.gmail.com', 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(gmailUser, gmailPassword)
    mailServer.sendmail(gmailUser, recipient, msg.as_string())
    mailServer.close()
    print "Mail sent"

    
mailer = MailSender()
mailer.send(to=["ornitorrinco@gmail.com"], subject="Ejemplo", body="Este deberia ser un correo ams interesante", cc=["abraham.alonzo@uabc.edu.mx"])

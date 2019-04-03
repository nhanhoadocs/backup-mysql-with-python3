import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging
logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', filename='/var/log/backup.log',level=logging.DEBUG, datefmt='%Y-%m-%d %H:%M:%S')

class EmailNotify(object):
    def __init__(self, settings, subject_date, email_content):
        self.smtp_server    = settings["email"]["smtp_server"]
        self.smtp_user      = settings["email"]["smtp_user"]
        self.smtp_password  = settings["email"]["smtp_password"]
        self.smtp_from      = settings["email"]["smtp_from"]
        self.smtp_TLS       = settings["email"]["smtp_TLS"]
        self.smtp_port      = int(settings["email"]["smtp_port"])
        self.email_subject  = settings["email"]["email_subject"]
        self.receiver_email = settings["email"]["receiver_email"]
        self.mail_datetime  = subject_date
        self.email_content  = email_content

    def send_email(self):
        message = MIMEMultipart("alternative")
        message["Subject"] = self.email_subject.format(self.mail_datetime)
        message["To"] = self.receiver_email
        message['From'] = self.smtp_from
        message.attach(MIMEText(self.email_content, "html"))

        if self.smtp_TLS is True:
            try:
                with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                    server.login(self.smtp_user , self.smtp_password)
                    server.sendmail(
                        self.smtp_user, self.receiver_email, message.as_string()
                    )
            except Exception as ex:
                logging.warning("email " + ex)          
        else:
            try:
                context = ssl.create_default_context()
                with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port, context) as server:
                    server.login(self.smtp_user , self.smtp_password)
                    server.sendmail(
                        self.smtp_user, self.receiver_email, message.as_string()
                    )
            except Exception as ex:
                logging.warning("email " + ex)
        
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class EmailService:
    def __init__(self, sender_email: str, gmail_app_password: str):
        self.sender_email = sender_email
        self.gmail_app_password = gmail_app_password
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587  # Port for TLS

    def send_email(self, recipient_email: str, subject: str, body: str) -> None:
        message = MIMEMultipart()
        message["From"] = self.sender_email
        message["To"] = recipient_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "html"))
        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.gmail_app_password)
                server.sendmail(self.sender_email, recipient_email, message.as_string())
            print("Email sent successfully!")
        except Exception as e:
            print(f"Failed to send email: {e}")

import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from main import scrape_article_data
from dotenv import load_dotenv

load_dotenv()


def send_email(subject, body, recipient):
    sender = os.getenv('EMAIL_SENDER')
    password = os.getenv('EMAIL_PASSWORD')

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.strato.de', 465)
        server.ehlo()  # Can be omitted
        server.starttls()  # This upgrades the connection to TLS
        server.ehlo()  # Can be omitted
        server.login(sender, password)
        server.send_message(msg)
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(sender, password, recipient)
        print(f"Error: {e}")


def main():
    URL = 'https://www.sciencenews.org/'
    scraped_data = scrape_article_data(URL)

    email_subject = "Scraped Data from Science News"
    email_body = "\n".join(scraped_data)
    recipient = "test@test.de"  # Replace with the recipient's email address
    send_email(email_subject, email_body, recipient)


if __name__ == "__main__":
    main()

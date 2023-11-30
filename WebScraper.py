import smtplib
import os

from WebScraper import scrape_article_data

from message_to_html import create_html_from_scraper
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv


def load_envfile():

    load_dotenv()
    print("Loading .env file...")

    try:
        sender = os.getenv('EMAIL_SENDER')
        password = os.getenv('EMAIL_PASSWORD')
        smtp_server = os.getenv('SMTP_SERVER')
        port = os.getenv("PORT")

        if sender and password and smtp_server and port:
            print(".env file was successfully loaded...")
            return sender, password, smtp_server, port
        else:
            config = {
                "EMAIL_SENDER": sender,
                "EMAIL_PASSWORD": password,
                "SMTP_SERVER": smtp_server,
                "PORT": port
            }
            for var_name, var_value in config.items():
                if not var_value:
                    print(f"{var_name} not set")

    except ValueError:
        print(f"Error loading the .env file:{ValueError}")


def send_email(receiver_email, subject):

    sender, password, smtp_server, port = load_envfile()

    message = MIMEMultipart()
    message["From"] = sender
    message["To"] = receiver_email
    message["Subject"] = subject

    html = create_html_from_scraper(
        scrape_article_data('https://www.sciencenews.org/'))

    message.attach(MIMEText(html, "html"))

    try:
        with smtplib.SMTP_SSL(smtp_server, port) as server:
            server.login(sender, password)
            server.sendmail(sender, receiver_email, message.as_string())
            print(
                f"Sending Mail to with subject {subject} to {receiver_email,}")

    except Exception as e:
        print(f"An error occurred: {e}")


send_email("@@@ADD_E-MAIL_ADRESS_HERE@@@", "sciencenews scraper_news")

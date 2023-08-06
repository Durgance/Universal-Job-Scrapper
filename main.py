from scrapper_careers import *
from mailer import *

if __name__ == "__main__":
    data = scrape()
    message = format_mail(data)
    send_mail(message)
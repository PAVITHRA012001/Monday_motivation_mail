from datetime import datetime
import smtplib
import random

my_email="kimme8733@gmail.com"
password="smhpcbgnteawzgmp"


def email_sender():
    with open("quotes.txt") as file_quote:
        allquotes = file_quote.readlines()
        quote = random.choice(allquotes)

    with smtplib.SMTP('smtp.gmail.com') as server:
        server.starttls()
        server.login(user=my_email, password=password)
        server.sendmail(
            from_addr=my_email,
            to_addrs="ppavi0932@gmail.com",
            msg=f"Subject:Today's Motivational Quote\n\n{quote}"
        )

weekday = datetime.now().weekday()#now gives current datetime
if weekday==0:#monday=0
    email_sender()
else:
    pass





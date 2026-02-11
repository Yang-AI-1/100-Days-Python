import smtplib
import datetime as dt
import random


my_email = "dylanstest01@gmail.com"
password = "xjsv imdu jhzd yqrf" #Dont share this.
#
#
# with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
#     connection.starttls() #Makes the connection secure.
#     connection.login(user=my_email,password=password)
#     connection.sendmail(from_addr=my_email,to_addrs="playsjay0@gmail.com",msg="Subject:New Greeting\n\nHi Dylan. Your not Jay.")
#     connection.close()

now = dt.datetime.now() #Gets you the current date and time
current_year = now.year
current_month = now.month
today = now.weekday() #Returns the index of the current day,counting from monday.

date_of_birth = dt.datetime(year=2007, month=8, day=11,hour=4)

with open("quotes.txt") as quotes:
    q_list = quotes.readlines()
    quote_list = [q.strip() for q in q_list]

# if today == 2: #wednesday index
#     random_quote = random.choice(quote_list)
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls() #security
#         connection.login(user= my_email, password=password)
#         connection.sendmail(from_addr= my_email, to_addrs="Nirinakaes@gmail.com", msg=f"Subject:A quote to encourage you.\n\n {random_quote}")
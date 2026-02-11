import pandas
import smtplib
import random
import datetime as dt
from pathlib import Path
from smtp_manager import *


birthday_info = pandas.read_csv("birthdays.csv")
birthday_dict = {(row["month"],row["day"]): row.to_dict() for _, row in birthday_info.iterrows()}

#Random file selection logic:
template_path = Path("C:/AI_Eng/100-Days-Python/Day32.SMTPlib_Emails/Birthday wisher/letter_templates")
files = [file for file in template_path.iterdir() if file.is_file()]
if not files:
    print(f"No file found in the directory")
random_template = random.choice(files)

#File opening and reading.
with open(random_template) as letter_template:
    letter = letter_template.read()
    
#my_info
my_email = "dylanstest01@gmail.com"
password = "xjsv imdu jhzd yqrf"

#Fetching the date and storing it in a tuple.
today = dt.datetime.now() #Returns a date object.
today_tuple = (today.month, today.day) #Accesses the month and day attributes.

birthdate = today_tuple 


if birthdate in birthday_dict:
    #Definition
    recipient_email = birthday_dict[birthdate].get("email")
    recipient_name = birthday_dict[birthdate].get("name")

    #Personalization
    ready_letter = letter.replace("[NAME]",recipient_name)
    smtp_domain = get_smtp_address(my_email)
    #Operation
    with smtplib.SMTP(smtp_domain) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=recipient_email,
                            msg=f"Subject:HAPPY BIRTHDAY\n\n{ready_letter}")









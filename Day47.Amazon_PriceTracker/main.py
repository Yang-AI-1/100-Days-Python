from bs4 import BeautifulSoup
import requests
import pprint as p
import smtplib
import dotenv
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

dotenv.load_dotenv()
PORT_NUMBER = 587
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SMTP_ADDRESS = os.getenv("SMTP_ADDRESS")
AMAZON_APP_PASSWORD = os.getenv("AMAZON_APP_PASSWORD")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")

#-------------------------- Webscraping Layer -----------------------------#
amazon_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
header = {"user-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36",
          "Accept-Language": "en-US"}

response = requests.get(url=amazon_url,headers=header)
response.raise_for_status()

web_data = response.text

soup = BeautifulSoup(web_data,"html.parser")

dollars = soup.select_one(".a-price-whole").get_text()
cents = soup.select_one(".a-price-fraction").get_text()

price_string = f"{dollars}{cents}"
product_price = float(price_string.replace(",",""))
product_name = soup.select_one("#productTitle").get_text()
currency_symbol = soup.select_one("#a-price-symbol").get_text()

#--------------- E-mail Layer--------------------#

if product_price < 15000:
    with smtplib.SMTP(SMTP_ADDRESS, port=PORT_NUMBER) as connection:
        connection.starttls()
        connection.login(user=SENDER_EMAIL,password=AMAZON_APP_PASSWORD)
        #Envelope
        msg = MIMEMultipart()
        msg["From"] = SENDER_EMAIL
        msg["TO"] = RECIPIENT_EMAIL
        msg["Subject"] = "Amazon Price Alert!!"
        #Body
        body = f"Get yourself the{product_name}\nPrice: {currency_symbol}{product_price}\nGet the product at: {amazon_url}"
        msg.attach(MIMEText(body,"plain","utf-8"))
        #sending
        connection.send_message(msg)

#TODO.Revisions:
# 1.Using the sendemail() method for the connection can process ascii characters so its prone to unix errors,
# Instead, using MIME(python inbuilt) allows you to format the message more freely and allows you to choose the message
# format e.g UTF-8 which I guess is a standard Library. You still using the same connection just with the send_message()
# method which accepts an MIMEmultipart() object.
# 2.Live websites change too much.
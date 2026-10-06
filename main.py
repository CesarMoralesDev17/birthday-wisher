# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


import pandas as pd
import os
from dotenv import load_dotenv
import datetime as dt
import smtplib
import random
load_dotenv()
# 1. Update the birthdays.csv
letters = ["./letter_templates/letter_1.txt","./letter_templates/letter_2.txt","./letter_templates/letter_3.txt"]
email_origin = os.getenv("GMAIL_ADR")
app_password = os.getenv("GMAIL_APP_PASSWORD")
# 2. Check if today matches a birthday in the birthdays.csv
dates_df = pd.read_csv("birthdays.csv")
now = dt.datetime.now()
possible_birthday = dates_df[dates_df.day == now.day]

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if possible_birthday.month.item() == now.month:
    letter_path = random.choice(letters)
    recipient_name = possible_birthday.name.item()  
    recipient_email = possible_birthday.email.item()
    with open(letter_path,mode="r") as letter_file:
        msg_letter = letter_file.read().replace("[NAME]",recipient_name)
# 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=email_origin,password=app_password)
        connection.sendmail(from_addr=email_origin,to_addrs=recipient_email,msg=f"Subject: Happy birthday!\n\n{msg_letter}")



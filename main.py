##################### Extra Hard Starting Project ######################
from datetime import datetime
import pandas
import random
import smtplib
import os
from dotenv import find_dotenv , load_dotenv

dotenv_path =  find_dotenv()
load_dotenv(dotenv_path)

MY_EMAIL = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("PASSWORD")

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")


for index, row in data.iterrows():
    day = row["day"]
    month = row["month"]
    if month == today_tuple[0] and day == today_tuple[1]:
        birthday_person = row
        file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
        with open(file_path) as letter_file:
            contents = letter_file.read()
            replaced_content = contents.replace("[NAME]", birthday_person["name"])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=birthday_person["email"],
                                msg=f"Subject:Happy birthday!\n\n{replaced_content}")

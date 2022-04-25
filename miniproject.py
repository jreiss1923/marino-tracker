import os
from dotenv import load_dotenv
import psycopg2
from bs4 import BeautifulSoup
import requests
import time
import traceback

load_dotenv()

conn = psycopg2.connect(
    host=os.environ.get("HOST"),
    database=os.environ.get("DATABASE"),
    user=os.environ.get("USER"),
    password=os.environ.get("PASSWORD")
)

cur = conn.cursor()

def scrape_marino():

    headers = {
        "User-Agent":
            "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"
    }

    response = requests.get("https://connect2concepts.com/connect2/?type=circle&key=2A2BE0D8-DF10-4A48-BEDD-B3BC0CD628E7", headers=headers)
    response_percent_centers = BeautifulSoup(response.text, 'html.parser').find_all('center')
    for center in response_percent_centers[1:-1]:
        main_text = center.text.strip("\n").split(" ")

        data_percent = center.find('div').attrs['data-percent']
        data_number = main_text[-4][:-8]
        gym_name = " ".join(main_text[:-6]) + " " + main_text[-6][:-10]
        date_str = format_date_iso(main_text[-3])
        date_time = date_str + " " + convert24(" ".join(main_text[-2:]))

        try:
            query = '''INSERT INTO percentage_count_timestamps(gym_name, percentage_occupied, total_in_area, count_time) VALUES (\'''' + gym_name + '''\', ''' + str(data_percent) + ''', ''' + str(data_number) + ''', TIMESTAMP \'''' + date_time + '''\')'''
            cur.execute(query)
            conn.commit()
        except Exception as e:
            conn.rollback()
            traceback_str = ''.join(traceback.format_exception(None, e, e.__traceback__))

def convert24(str1):
    # Checking if last two elements of time
    # is AM and first two elements are 12
    if str1[-2:] == "AM" and str1[:2] == "12":
        return "00" + str1[2:-2]

    # remove the AM
    elif str1[-2:] == "AM":
        return str1[:-2]

    # Checking if last two elements of time
    # is PM and first two elements are 12
    elif str1[-2:] == "PM" and str1[:2] == "12":
        return str1[:-2]

    else:
        # add 12 to hours and remove PM
        return str(int(str1[:2]) + 12) + str1[2:-2]

def format_date_iso(date):
    date_arr = date.split("/")
    date_arr = date_arr[2] + "-" + date_arr[0] + "-" + date_arr[1]
    return date_arr

while(True):
    scrape_marino()
    time.sleep(300)

import os
from dotenv import load_dotenv
import psycopg2
from bs4 import BeautifulSoup
import requests
import time
import traceback

load_dotenv()

conn = psycopg2.connect(
    host=os.environ.get("HOST"),
    database=os.environ.get("DATABASE"),
    user=os.environ.get("USER"),
    password=os.environ.get("PASSWORD")
)

cur = conn.cursor()

def scrape_marino():

    headers = {
        "User-Agent":
            "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"
    }

    response = requests.get("https://connect2concepts.com/connect2/?type=circle&key=2A2BE0D8-DF10-4A48-BEDD-B3BC0CD628E7", headers=headers)
    response_percent_centers = BeautifulSoup(response.text, 'html.parser').find_all('center')
    for center in response_percent_centers[1:-1]:
        main_text = center.text.strip("\n").split(" ")

        data_percent = center.find('div').attrs['data-percent']
        data_number = main_text[-4][:-8]
        gym_name = " ".join(main_text[:-6]) + " " + main_text[-6][:-10]
        date_str = format_date_iso(main_text[-3])
        date_time = date_str + " " + convert24(" ".join(main_text[-2:]))

        try:
            query = '''INSERT INTO percentage_count_timestamps(gym_name, percentage_occupied, total_in_area, count_time) VALUES (\'''' + gym_name + '''\', ''' + str(data_percent) + ''', ''' + str(data_number) + ''', TIMESTAMP \'''' + date_time + '''\')'''
            cur.execute(query)
            conn.commit()
        except Exception as e:
            conn.rollback()
            traceback_str = ''.join(traceback.format_exception(None, e, e.__traceback__))

def convert24(str1):
    # Checking if last two elements of time
    # is AM and first two elements are 12
    if str1[-2:] == "AM" and str1[:2] == "12":
        return "00" + str1[2:-2]

    # remove the AM
    elif str1[-2:] == "AM":
        return str1[:-2]

    # Checking if last two elements of time
    # is PM and first two elements are 12
    elif str1[-2:] == "PM" and str1[:2] == "12":
        return str1[:-2]

    else:
        # add 12 to hours and remove PM
        return str(int(str1[:2]) + 12) + str1[2:-2]

def format_date_iso(date):
    date_arr = date.split("/")
    date_arr = date_arr[2] + "-" + date_arr[0] + "-" + date_arr[1]
    return date_arr

while(True):
    scrape_marino()
    time.sleep(300)

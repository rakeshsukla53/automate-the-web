import time
import os
from faker import Faker
from hashlib import md5
from datetime import datetime
from time import time

EMAIL = os.environ['EMAIL']
PASSWORD = os.environ['PASSWORD']


def scroll_to_bottom(driver):
    pause_time = 0.8
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
        time.sleep(pause_time)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


def scroll_few_pages(driver, pages=10):
    pause_time = 1.5
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    count = 0
    while True and count <= pages:
        # Scroll down to bottom
        count += 1
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
        time.sleep(pause_time)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


def close_all_popups(driver):
    for h in driver.window_handles[1:]:
        driver.switch_to_window(h)
        driver.close()
    driver.switch_to_window(driver.window_handles[0])


def generate_first_name():
    return Faker().first_name()


def generate_last_name():
    return Faker().last_name()


def generate_single_email(email_address='lollol@lol.com'):
    """Generates a single unique email address. Defaults if no value is passed."""
    email = email_address.split('@')
    return '{}+{}@{}'.format(email[0],
                             md5(datetime.now().strftime("%Y%m%d%H%M%f").encode('ascii')).hexdigest(),
                             email[1])


def generate_password():
    return 'S@IOmlakasimlaka123sim'

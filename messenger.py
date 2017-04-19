from selenium import webdriver
from time import sleep
from common import *


def spam_messenger():
    driver = webdriver.Chrome()
    driver.set_window_size(1640, 1640)
    driver.maximize_window()
    driver.get('https://www.messenger.com/')
    driver.find_element_by_css_selector('input[placeholder="Email or phone number"]').send_keys(EMAIL)
    driver.find_element_by_css_selector('input[placeholder="Password"]').send_keys(PASSWORD)
    driver.find_element_by_css_selector('button[name="login"]').click()
    sleep(3)
    list_of_friends = driver.find_elements_by_css_selector('ul[aria-label="Conversation List"]>li')
    scroll_to_bottom(driver)
    total_friends = len(list_of_friends)
    for index, friend in enumerate(list_of_friends):
        if index == total_friends - 1:
            sleep(15)
        friend.click()
    driver.quit()

if __name__ == '__main__':
    spam_messenger()


# driver.find_element_by_css_selector('div[aria-label="Type a message..."]').send_keys('This is an automated message '
                                                                                     #  'from chat bot. Please ignore')
# this works for all ... messenger chat bot





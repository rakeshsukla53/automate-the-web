from selenium import webdriver
from common import *
from selenium.webdriver.chrome.options import Options
from time import sleep


def create_reddit_profile():
    options = Options()
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(chrome_options=options)
    driver.set_window_size(1640, 1640)
    driver.maximize_window()
    driver.get('https://www.reddit.com/')
    title = 'a[data-event-action="title"]'
    score_dislikes = '.score.dislikes'
    title_thumbnail = 'a[data-event-action="thumbnail"]'
    reddit_link = 'div[data-type="link"]'
    submit_a_new_link = '[data-event-detail="self"]'
    user_name = 'input[id="user_login"]'
    password = 'input[id="passwd_login"]'
    login = 'span[class="c-form-throbber"] + button[tabindex="3"]'
    enter_title = 'textarea[name="title"]'
    text_area = 'textarea[rows="1"]'
    funny_area = 'input[id="sr-autocomplete"]'
    recaptcha = '.recaptcha-checkbox-checkmark'
    recaptcha_title = 'span[class="recaptcha-checkbox"]'
    driver.find_element_by_css_selector(title)

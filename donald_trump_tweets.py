from selenium import webdriver
from common import *
from selenium.webdriver.chrome.options import Options


def get_donald_trump_tweets():
    options = Options()
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(chrome_options=options)
    driver.set_window_size(1640, 1640)
    driver.maximize_window()
    driver.get("https://twitter.com/realDonaldTrump")
    scroll_few_pages(driver, pages=1000)
    driver.find_element_by_xpath('//*[contains(text(), "Back to top")]').click()
    sleep(2)
    all_the_tweets = driver.find_elements_by_css_selector('.js-tweet-text-container > p')
    for tweet in all_the_tweets:
        print(tweet.get_attribute('innerText'))

if __name__ == '__main__':
    get_donald_trump_tweets()

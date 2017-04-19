from selenium import webdriver
from common import *
from selenium.webdriver.chrome.options import Options


def scrape_facebook_page():
    options = Options()
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(chrome_options=options)
    driver.set_window_size(1640, 1640)
    driver.maximize_window()
    driver.get("https://facebook.com")
    email = os.environ['EMAIL']
    password = os.environ['PASSWORD']
    driver.find_element_by_css_selector('input[name="email"]').send_keys(email)
    driver.find_element_by_css_selector('input[data-testid="royal_pass"]').send_keys(password)
    driver.find_element_by_css_selector('input[data-testid="royal_pass"]').submit()
    time.sleep(2)
    driver.find_element_by_xpath('//*[text()="Hackathon Hackers"]').click()
    scroll_few_pages(driver, pages=100)
    hack_data = driver.find_elements_by_css_selector('.userContent p')
    for data in hack_data:
        print(data.get_attribute('innerHTML'))
    driver.quit()

if __name__ == '__main__':
    scrape_facebook_page()
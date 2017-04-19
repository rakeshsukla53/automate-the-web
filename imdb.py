from selenium import webdriver
from common import *
from selenium.webdriver.chrome.options import Options
from time import sleep


def create_fake_imdb_profile():
    options = Options()
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(chrome_options=options)
    driver.set_window_size(1640, 1640)
    driver.maximize_window()
    driver.get('https://www.imdb.com/registration/signin')
    driver.find_element_by_xpath('//a[text()="Create a New Account"]').click()
    name = '{} {}'.format(generate_first_name(), generate_last_name())
    email = generate_single_email()
    driver.find_element_by_id("ap_customer_name").send_keys(name)
    driver.find_element_by_id("ap_email").send_keys(email)
    driver.find_element_by_id("ap_password").send_keys("dfbidfj[dk[kskssm")
    driver.find_element_by_id("ap_password_check").send_keys("dfbidfj[dk[kskssm")
    # this worked
    driver.find_element_by_css_selector('input[type="submit"]').click()
    sleep(2)
    driver.find_element_by_id('navbar-query').send_keys('Westworld')
    sleep(2)
    westworld_url = driver.find_element_by_xpath('//div[@id="navbar-suggestionsearch"]/a').get_attribute('href')
    driver.get(westworld_url)
    element = driver.find_element_by_class_name('star-rating-button')
    driver.execute_script("arguments[0].setAttribute('class','star-rating-button open')", element)
    driver.find_element_by_xpath("//*[@class='star-rating-stars']/a[10]").click()
    element = driver.find_element_by_class_name('star-rating-button')
    driver.execute_script("arguments[0].setAttribute('class','star-rating-button')", element)
    sleep(3)
    driver.quit()

if __name__ == '__main__':
    create_fake_imdb_profile()

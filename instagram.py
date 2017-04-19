from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from common import *


def download_photos_instagram():
    options = Options()
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(chrome_options=options)
    driver.set_window_size(1640, 1640)
    driver.maximize_window()
    driver.get("https://www.instagram.com/lifewithspices/")
    driver.find_element_by_xpath('//*[contains(text(), "Load more")]').click()
    scroll_few_pages(driver, pages=1000)
    all_images = driver.find_elements_by_css_selector('._jjzlb > img')
    for image_url in all_images:
        print(image_url.get_attribute('src'))


if __name__ == '__main__':
    download_photos_instagram()

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class GoDjango(object):
    pro_video_tag = '.media.episode-list-item.padding-15 div div span'
    video_container = '.media.episode-list-item.padding-15'
    first_video_title = 'h4[class="media-heading"] a'
    next_button_click = 'li[class="active"] + li a'
    video_download_link = 'div[class="video-description"] + iframe'


def download_videos():
    """ download all videos from www.godjango.com """
    options = Options()
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(chrome_options=options)
    driver.set_window_size(1640, 1640)
    driver.maximize_window()
    driver.get('https://godjango.com/browse/')
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, GoDjango.first_video_title)))
    list_of_video_links = []
    
    while True:
        all_video_elements = driver.find_elements_by_css_selector(GoDjango.first_video_title)
        for link in all_video_elements:
            list_of_video_links.append(link.get_attribute('href'))
        driver.execute_script("window.scrollTo(0, 4650);")
        try:
            driver.find_element_by_css_selector(GoDjango.next_button_click).click()
        except:
            print('we have reached the end of page')
            break

    for video_url in list_of_video_links:
        driver.get(video_url)
        try:
            print(driver.find_element_by_css_selector(GoDjango.video_download_link).get_attribute('src'))
        except:
            print("Video is private")

if __name__ == '__main__':
    download_videos()

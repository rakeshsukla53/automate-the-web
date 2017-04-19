from selenium import webdriver
from time import sleep


def send_message_whatsapp():
    web = webdriver.Chrome()
    web.get('http://web.whatsapp.com')
    sleep(15)
    elem = web.find_element_by_xpath('//span[contains(text(), "Margi Malhotra")]')
    # the xpath can be replaced by //span[contains(., "Margi Malhotra")]
    # it can be replaced by //span[text()="Margi Malhotra "]
    elem.click()
    elem1 = web.find_elements_by_class_name('input')
    while True:
        elem1[1].send_keys('Automated text message from Bot. Please ignore!')
        web.find_element_by_class_name('compose-btn-send').click()

if __name__ == '__main__':
    send_message_whatsapp()
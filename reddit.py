from selenium import webdriver

driver = webdriver.Chrome()
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
